import os
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from answer import openai_create

# Put your telegram bot token as an environment variable named TOKEN
key = os.environ['TOKEN']
print("Bot has Started....")


def introduce(name):
  print(f'Hi {name}')


def start_command(update, context):
  update.message.reply_text("""Hello I am Baby Care Bot!
  You can ask me anything related to baby care and pregnancy.
  Commands:
  /start : To start the bot
  /help  : To get info about the bot commands
  /question : To ask a question""")


def help_command(update, context):
  update.message.reply_text("""Help menu:
  /start : To start the bot
  /help  : To get info about the bot commands
  /question : To ask a question
  """)


def question_command(update, context):
  update.message.reply_text("Ask your question!")


def handle_message(update, context):
  text = str(update.message.text).lower()
  response = openai_create(text)
  update.message.reply_text(response)


def error(update, context):
  print(f"Update {update} caused error {context.error}")


def main():
  updater = Updater(key, use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start_command))

  dp.add_handler(CommandHandler("help", help_command))

  dp.add_handler(CommandHandler("question", question_command))

  dp.add_handler(MessageHandler(Filters.text, handle_message))

  dp.add_error_handler(error)

  updater.start_polling()
  updater.idle()


main()