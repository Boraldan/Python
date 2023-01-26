
import user_interfeice as ui
import logger as lr


def select():
    ui.menu()
    value = ui.enter('Введите номер запроса --->  ')
    if value == '1':
        lr.view_all()
    elif value == '2':
        value = ui.enter('Введите Фамилию и/или Имя (через пробел): ')
        lr.view_one(value)
    elif value == '3':
        value = ui.enter('Введите Фамилие, Имя, Телефон, Описание(через пробелы): ')
        lr.add_one(value)
    elif value == '4':
        value = ui.enter('Введите Фамилию: ')
        lr.get_xml(value)
    elif value == '5':
        value = ui.enter('Введите Фамилию и/или Имя (через пробел): для удалени контакта: ')
        lr.remove_one(value)
    elif value == '6':
        lr.remove_all()
    elif value == '7':
        lr.import_base()