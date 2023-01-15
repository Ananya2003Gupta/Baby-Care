import gradio as gr
from answer import openai_create

prompt = """Ask your question!"""


def chatgpt_clone(input, history):
  history = history or []
  s = list(sum(history, ()))
  s.append(input)
  inp = ' '.join(s)
  output = openai_create(inp)
  history.append((input, output))
  return history, history


block = gr.Blocks()

with block:
  gr.Markdown("<h1><center>Baby Care Web 👶🏻</center></h1>")
  gr.Markdown(
    "<p><center>Baby Care Web is here to assist you and answer all your queries related to pregnancy, childbirth, the baby's growth, health, and nutrition, the mother's health, parenting tips, and more</center></p>"
  )
  chatbot = gr.Chatbot()
  message = gr.Textbox(placeholder=prompt)
  state = gr.State()
  submit = gr.Button("SEND")
  submit.click(chatgpt_clone,
               inputs=[message, state],
               outputs=[chatbot, state])

block.launch(debug=True) #to get public link put share=True as a parameter in launch