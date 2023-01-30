# Модуль записи логов

def write_data(data): # запись логов
    with open('DZ9_bot_X0\\calc\\log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(data + '\n')
