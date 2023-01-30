from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# app = ApplicationBuilder().token("5816495751:AAFsTEkFkFjI3najCAwEwm6CpowLQjb7sf4").build()

# app.add_handler(CommandHandler("hello", hello))
# print('server star
# app.run_polling()
# ----------------------------------------------------
 # This installs the latest stable release
#  pip install python-telegram-bot --upgrade
#  python bot.py

#  Базовые настройки бота, что сверху  ----------------------

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/help\n/exo')

app = ApplicationBuilder().token("5816495751:AAFsTEkFkFjI3najCAwEwm6CpowLQjb7sf4").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))

print('server start')

app.run_polling()