from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import csv
import xml_generator as xml


file_path = 'DZ9_bot_X0\\tel_dict\\telbase.txt'             # вписать свой путь к базе
import_file = 'DZ9_bot_X0\\tel_dict\\import_telbase.txt'    # вписать свой путь к базе

async def view_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  # ok
    st = ''
    with open(file_path, mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')  
        for row in data:   
            st += '  '.join(row) + '\n'

    await update.message.reply_text(st)


async def viview_one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   # ok
    text = update.message.text
    st = 'Фамилия Имя Телефон Описание\n'
    find = text.strip(" ,/")
    find = find.replace('  ', ' ').split()
    find = find[1:]
    with open(file_path, mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        flag = False
        for row in data:   
            if len(find) == 2 and find[0].lower() in str(row[0]).lower() and find[1].lower() in str(row[1]).lower():
                st += ' '.join(row) + '\n'
                flag = True
            elif len(find) == 1 and find[0].lower() in str(row).lower():
                st += ' '.join(row) + '\n'
                flag = True
        if flag == False:
            st ='Нет записи с такими данными'

    await update.message.reply_text(st)


async def add_one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  # ok
    text = update.message.text
    text = text.replace('  ', ' ').strip(" ,")
    text = text.replace(' ', ',') + '\n'
    text = text[9:]
    with open(file_path, "a", encoding='utf-8') as file:
        file.write(text)

    await update.message.reply_text('Контакт добавлен')


async def export_XML(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   # ok
    text = update.message.text
    st = 'Фамилия Имя Телефон Описание\n'

    find = text.strip(" ,/")
    find = find.replace('  ', ' ').split()
    find = find[1:]
    with open(file_path, mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        flag = False
        for row in data:   
            if len(find) == 2:
                if len(find) == 2 and find[0].lower() in str(row[0]).lower() and find[1].lower() in str(row[1]).lower():
                    xml.create(row)
                    st += ' '.join(row) + '--> экспортирован XML'
                    flag = True
            else:
                await update.message.reply_text('Неправильный ввод. Введите Фамилию и Имя через пробел')
                break

        if flag == False:
            st ='Нет записей с такими данными'

    await update.message.reply_text(st)


async def dell_one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   # ok
    text = update.message.text
    st = 'Фамилия Имя Телефон Описание\n'

    find = text.strip(" ,/")
    find = find.replace('  ', ' ').split()
    find = find[1:]
    li = []
    with open(file_path, mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        flag = False
        for row in data:   
            if len(find) == 2:
                if find[0].lower() in str(row[0]).lower() and find[1].lower() in str(row[1]).lower():
                    st += ' '.join(row) + '--> контакт удален'
                    flag = True
                else:
                    li.append(row)
            else:
                await update.message.reply_text('Неправильный ввод. Введите Фамилию и Имя через пробел')
                break

    if flag == True:
        with open(file_path, mode="w", encoding='utf-8') as file:
            data = csv.writer(file, delimiter = ",", lineterminator="\r")
            for row in li:
                data.writerow(row)
    else: 
        st ='Нет записей с такими данными'

    await update.message.reply_text(st)

async def import_base(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   # ok
    li_imp = []
    li_base = []
    with open(import_file, mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        for row in data:
            li_imp.append(row)

    with open(file_path, mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')
        for row in data:
            li_base.append(row)

    for row in li_imp:
        if not str(row).lower() in str(li_base).lower():
            li_base.append(row)

    with open(file_path, mode="w", encoding='utf-8') as file:
        data = csv.writer(file, delimiter = ",", lineterminator="\r")
        for row in li_base:
            data.writerow(row)

    await update.message.reply_text('Контакты импортированы')