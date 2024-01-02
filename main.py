from telegram.ext import CommandHandler, MessageHandler, filters, Application
from telegram import Update
from googletrans import Translator

# instantiating instance of telebot and translator
curr_token = ""
updater = Application.builder().token(curr_token).build()
translator = Translator(service_urls=["translate.google.com"])

# start  
async def start(update, context):
    await update.message.reply_text("Hallo Schatz!")

# define capabilities (translate en -> de)
async def translate(update, context):
    message = update.message.text
    translated_msg = translator.translate(message, dest="de", src="auto").text
    await update.message.reply_text(translated_msg)

# define handlers 
updater.add_handler(CommandHandler('start', start))
updater.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

# idle actions 
updater.run_polling(allowed_updates= Update.ALL_TYPES)
