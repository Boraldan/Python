from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands


app = ApplicationBuilder().token("5816495751:AAFsTEkFkFjI3najCAwEwm6CpowLQjb7sf4").build()

print('Сервер запустился')

app.add_handler(CommandHandler("g_1", bot_commands.g_1))

app.run_polling()