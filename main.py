from telegram.ext import CommandHandler, MessageHandler, filters, Application
from telegram import Update
import goslate

# instantiating instance of telebot and translator
curr_token = ""
updater = Application.builder().token(curr_token).build()
gs = goslate.Goslate()

# define capabilities 
async def start(update, context):
    await update.message.reply_text("Hallo Schatz!")

async def translate(update, context):
    message = update.message.text
    translated_msg = gs.translate(message, 'de')
    await update.message.reply_text(translated_msg)

# define handlers 
updater.add_handler(CommandHandler('start', start))
updater.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

# idle actions 
updater.run_polling(allowed_updates= Update.ALL_TYPES)
