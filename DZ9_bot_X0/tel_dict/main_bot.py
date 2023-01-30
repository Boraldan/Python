
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import base_bot as bb

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'''Команды для действий:
    /view_all - посмотреть все контакты
    /view_one - посмотреть один контакт - Введите Фамилию и Имя (через пробел)
    /add_one - добавить один - Введите Фамилие, Имя, Телефон, Описание(через пробелы):
    /export_XML - экспорт XML одного контакта - Введите Фамилие и Имя (через пробелы):
    /dell_one  - удалить контакт - Введите Фамилие и Имя (через пробелы)
    /import_base  - импортировать контакты''')

app = ApplicationBuilder().token("   !!!   введидет ваш токен  !!!   ").build()
 
app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("view_all", bb.view_all))
app.add_handler(CommandHandler("view_one", bb.viview_one))
app.add_handler(CommandHandler("add_one", bb.add_one))
app.add_handler(CommandHandler("export_XML", bb.export_XML))
app.add_handler(CommandHandler("dell_one", bb.dell_one))
app.add_handler(CommandHandler("import_base", bb.import_base))

print('start server')

app.run_polling() 