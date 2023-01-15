#open ai api to get answers like chatgpt

import os
import openai

#Put your open api key as an environment variable named OPENAI_API_KEY
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
openai.api_key = OPENAI_API_KEY

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def openai_create(prompt):

  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=prompt,
                                      temperature=0.9,
                                      max_tokens=125,
                                      top_p=1,
                                      frequency_penalty=0,
                                      presence_penalty=0.6,
                                      stop=[" Human:", " AI:"])

  return response.choices[0].text