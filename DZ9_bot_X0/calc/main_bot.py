# Прикрутить бота к задачам с предыдущего семинара:

#     Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
#     Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import calcul as ca
import time
import log_generate as lg

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lg.write_data(f'Получена команда /hi от {update.effective_user.first_name} ' + time.strftime('%d.%m.%y %H:%M:%S'))
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lg.write_data(f'Получена команда /menu от {update.effective_user.first_name} ' + time.strftime('%d.%m.%y %H:%M:%S'))
    await update.message.reply_text(f'Команды для действий:\n /Hi\n/menu\n/calc (например 5+5)')


app = ApplicationBuilder().token("                !!!!!!!!!!!!! ваш токен               ").build()
# app = ApplicationBuilder().token("  вставить свой токен сюда  !!! ").build()

app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("calc", ca.calc))
app.add_handler(CommandHandler("menu", menu))

print('start server')

app.run_polling() 

