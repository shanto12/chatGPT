# email_handler.py

import imaplib
import email

class EmailHandler:
    def __init__(self, credentials):
        self.credentials = credentials
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self.imap.login(credentials.email, credentials.password)

    def get_recruiter_email(self, subject):
        self.imap.select("inbox")
        result, data = self.imap.search(None, f'SUBJECT "{subject}"')
        email_ids = data[0].split()
        latest_email_id = email_ids[-1]
        result, email_data = self.imap.fetch(latest_email_id, "(RFC822)")
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)
        return email_message

    def send_response_email(self, to, subject, body, attachments):
        message = MIMEMultipart()
        message["From"] = self.credentials.email
        message["To"] = to
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        for attachment in attachments:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(open(attachment, "rb").read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",
                            f"attachment; filename={attachment}")
            message.attach(part)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.credentials.email, self.credentials.password)
        text = message.as_string()
        server.sendmail(self.credentials.email, to, text)
        server.quit()
