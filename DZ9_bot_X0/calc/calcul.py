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

    text = text.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')\
        .replace('(', '( ')\
        .replace(')', ' )').split()
    
    text = text[2:]

    text = [int(elem) if elem.isdigit() else elem for elem in text]
    text = [complex(el) if 'j' in str(el)  else el for el in text]

    while '(' in text:
        first_i = len(text) - text[::-1].index('(') - 1
        second_i = first_i + text[first_i:].index(')')
        text = text[:first_i] + f_calc(text[first_i + 1:second_i]) + text[second_i+1:]

    text = f_calc(text)

    lg.write_data(f'Отправлен ответ {str(text[0])} для {update.effective_user.first_name} '\
    + time.strftime('%d.%m.%y %H:%M:%S'))

    await update.message.reply_text(f'{str(text[0])}')