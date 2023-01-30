from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands


app = ApplicationBuilder().token("       !!!             ").build()

print('Сервер запустился')

app.add_handler(CommandHandler("g_1", bot_commands.g_1))

app.run_polling()