# import openai
# from CONSTS import API_KEY
# import requests
#
# # Set API key
# openai.api_key = API_KEY
#
# # Define the prompt
# prompt = """
# give a generic outline of a movie story?
#
#
#
#
#
# model = "text-davinci-003"
#
# #
# # # Generate a response from ChatGPT
# # response = openai.Completion.create(
# #     engine="text-davinci-003",
# #     prompt=prompt,
# #     max_tokens=1024,
# #     n=1,
# #     stop=None,
# #     temperature=0.5
# # )
#
# response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024)
#
#
# # Print the response
# print(response["choices"][0]["text"])
#
#
# #
# # import os
# # import openai
# #
# # openai.api_key = os.getenv("OPENAI_API_KEY")
# #
# # response = openai.Completion.create(
# #   model="text-davinci-003",
# #   prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",
# #   temperature=0,
# #   max_tokens=100,
# #   top_p=1,
# #   frequency_penalty=0.0,
# #   presence_penalty=0.0,
# #   stop=["\n"]
# # )
