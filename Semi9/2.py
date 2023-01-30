from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands


app = ApplicationBuilder().token("5841865362:AAGe-mekNEv9gYIPrV8kxAA6eNihfpSGJrU").build()
print('Сервер запустился')

app.add_handler(CommandHandler("g_1", bot_commands.g_1))


app.run_polling()


\

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

base = 2021
player = 1

async def g_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global player
    global base
    if base > 0:
        await update.message.reply_text(f'На столе {base} конфет.')
        await update.message.reply_text(f'Игрок {player} введите количество конфет сколько Вы возьмете: ')
        text = update.message.text.split()
        text = int(text[1])
        base -= text
        if base <= 0:
            await update.message.reply_text(f'На столе не осталось конфет, вы выиграли!.')
        else:
            await update.message.reply_text(f'На столе отсалось {base} конфет.')
        player = 3-player
    else:
        await update.message.reply_text('Конфеты кончились, отстань.')
