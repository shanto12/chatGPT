# main.py

import email_handler
import document_handler
import chatgpt_handler

def main():
    # Get the latest email from the recruiter
    email = email_handler.get_latest_email_from_recruiter()
    # Get the attachments from the email
    attachments = email_handler.get_attachments_from_email(email)
    # Get the resume from the data folder
    resume = document_handler.get_resume()
    # Get the response to the questions
    response = chatgpt_handler.get_response_to_questions(attachments, resume)
    # Save the response in the data/responses folder
    document_handler.save_response(response)
    # Send the email back to the recruiter with the response
    email_handler.send_response_email(email, response)

if __name__ == '__main__':
    main()
