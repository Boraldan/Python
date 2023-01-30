# **Задача:** при помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 2. Создайте программу для игры с конфетами человек против человека.
    
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#      Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#      Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
#       первому игроку, чтобы забрать все конфеты у своего конкурента?
    
#     a) Добавьте игру против бота
    
#     b) Подумайте как наделить бота "интеллектом"

pip install matplotlib
pip freeze
pip freeze > requirements.txt
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

py -m venv
py -m pip install
pip install -r requirements.txt
PowerShell


pip install virtualenv # установка пакета виртуального окружения
python -m venv venv # - создать виртуальное окружение
# source venv/bin/activate - активация ВО для линукс
venv\Scripts\activate # - активация в виндоус (обязательно \ - обратный слэш)
deactivate # - деактивация виртуального окружения
pip freeze # - распечатает установленные пакеты(библиотеки) (создаёт файл зависимостей)
pip install -U pip setuptools # - U-сокращенно upgrade, далее следуют имя или имена модулей, которые требуется обновить,
# в данном случае setuptools
python.exe -m pip install -U pip setuptools #- тоже самое
pip install requests lxml # - установка библиотек requests и lxml - если нужно установить несколько библиотек,
# то можно перечислить их через пробел
pip uninstall lxml -y # - удаление библиотеки, в данном случае lxml
pip uninstall -y -r requirements.txt # - удаляет все библиотеки, которые были прописаны в файле requirements.txt
pip freeze > requirements.txt # - создаёт файл с зависимостями (в нём прописываются все библи


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f' {update.effective_user.first_name}')



app = ApplicationBuilder().token("token").build()
app.add_handler(CommandHandler("hello", hello))

app.run_polling()
