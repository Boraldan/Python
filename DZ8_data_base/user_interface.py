# import export_data as ed
import import_data as id
import logger as lr
import xml_generator as xml

def user_choose():
    print('''Добро пожаловать в справочник школы! 
                Выберите действие:  
                1.Добавить   
                2.Редактировать   
                3.Удалить студента
                4.Вывести в консоль базу
                5.Экспорт в XML
                6.Поиск студента в базе по ФИО
                7.Выход''')
    choose = input("Введите цифру выбора: ")
    if choose == '1':
        print('''Выберите действие:
                1. Добавить ученика
                2. Добавить класс''')
        choose_2 = input("Введите цифру выбора: ")
        if choose_2 == '1':
            id.create_student()
        elif choose_2 == '2':
            classes = lr.get_class()
            name, classes = id.create_cl('-', classes)
            lr.set_classes(classes)
    elif choose == '2':
        print('''Выберите действие:
                1. Редактировать ученика
                2. Перевести в другой класс''')
        choose_3 = input("Введите цифру выбора: ")
        if choose_3 == '1':
            id.edit_student()
        elif choose_3 == '2':
            id.change_class()
    elif choose == '3':
        id.delete_student()
        user_choose()
    elif choose == '4':
        print('''Выберите действие:
                1. Список студентов
                2. Список классов''')
        choose_4 = input("Введите цифру выбора: ")
        if choose_4 == '1':
            lr.print_data(lr.get_students())
        elif choose_4 == '2':
            lr.print_class(lr.get_class())
    elif choose == '5':
        xml.create()
    elif choose == '6':
        value = input('Введите Фамилию и/или Имя (через пробел): ')
        id.view_one(value)
    elif choose == '7':
        return
    else:
        print("Вы ввели некорректное значение, повторите ввод!")
        user_choose()
