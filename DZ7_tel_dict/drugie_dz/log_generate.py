# Модуль записи логов

def write_data(data): # Функция записи логов
    with open('log.xml', 'a', encoding='utf-8') as log_file:
        log_file.write(data + '\n')
