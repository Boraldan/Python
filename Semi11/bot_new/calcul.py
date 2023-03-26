from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
import log_generate as lg

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    def f_calc(my_list):
        while '*' in my_list or '/' in my_list:
            for i in range(1, len(my_list), 2):
                if my_list[i] == '*':
                    result = my_list.pop(i+1) * my_list.pop(i-1)
                    my_list[i-1] = result
                    break
                elif my_list[i] == '/':
                    result = my_list.pop(i-1) / my_list.pop(i)
                    my_list[i-1] = result
                    break

        while '+' in my_list or '-' in my_list:
            for i in range(1, len(my_list), 2):
                if my_list[i] == '-':
                    result = my_list.pop(i-1) - my_list.pop(i)
                    my_list[i-1] = result
                    break
                elif my_list[i] == '+':
                    result = my_list.pop(i+1) + my_list.pop(i-1)
                    my_list[i-1] = result
                    break
        return my_list

    text = update.message.text
    lg.write_data(f'Получена команда {text} от {update.effective_user.first_name} '\
        + time.strftime('%d.%m.%y %H:%M:%S'))
    
    print(text)

    text = text.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')\
        .replace('(', ' ( ')\
        .replace(')', ' ) ').split()

    print(text)

    new_text = []
    flag = True
    count = 0

    for i, el in enumerate(text):
        if text[0].isdigit() or '(' in text[0]: 
            if el.isdigit():
                new_text.append(int(el))
            elif 'j' in el:
                new_text.append(complex(el))
            elif (("+" in el or "-" in el or "*" in el or "/" in el) and (str(new_text[i-1])).isdigit()) \
                or (("+" in el or "-" in el or "*" in el or "/" in el) and ')' in new_text[i-1]):
                new_text.append(el)
            elif "(" in el or ")" in el:
                new_text.append(el)
                count += 1
            else:
                flag = False
                break
        else:
            flag = False
            break

    if count%2:
        flag = False

    
    if flag:
        while '(' in new_text:
            first_i = len(new_text) - new_text[::-1].index('(') - 1
            second_i = first_i + new_text[first_i:].index(')')
            new_text = new_text[:first_i] + f_calc(new_text[first_i + 1:second_i]) + new_text[second_i+1:]

        new_text = f_calc(new_text)

        lg.write_data(f'Отправлен ответ {str(new_text[0])} для {update.effective_user.first_name} '\
        + time.strftime('%d.%m.%y %H:%M:%S'))

        await update.message.reply_text(f'{str(new_text[0])}')

    else:
        await update.message.reply_text(f'Такой пример {text} не могу решить.')