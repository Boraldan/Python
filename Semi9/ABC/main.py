from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def wo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.split()
    st = ''
    for el in text[1:]:
        if not 'abc'in el:
            st += str(el) + ' '
    
    # text = ' '.join(list(filter(lambda x: 'abc' not in x, text)))   #  еще вариант преобразования

    await update.message.reply_text(f'{st}')

app = ApplicationBuilder().token("5816495751:AAFsTEkFkFjI3najCAwEwm6CpowLQjb7sf4").build()

print('start server')

app.add_handler(CommandHandler("wo", wo))
app.add_handler(CommandHandler("hi", hi))


app.run_polling()


