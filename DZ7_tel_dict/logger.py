import csv
import xml_generator as xml

def view_all(): # 1
    with open('DZ7_tel_dict\\telbase.txt', mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')  
        for row in data:   
                print(*row)

def view_one(find): # 2
    with open('DZ7_tel_dict\\telbase.txt', mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        print('Фамилия Имя Телефон Описание')
        flag = False
        find = find.strip(" ,")
        find = find.replace('  ', ' ').split() 
        for row in data:   
            if len(find) == 2 and find[0].lower() in str(row[0]).lower() and find[1].lower() in str(row[1]).lower():
                print(*row)
                flag = True
            elif len(find) == 1 and find[0].lower() in str(row).lower():
                print(*row)
                flag = True
        if flag == False:
            print('Нет записи с такими данными')

def add_one(text): # 3
    with open('DZ7_tel_dict\\telbase.txt', "a", encoding='utf-8') as file:
        text = text.replace('  ', ' ').strip(" ,")
        text = text.replace(' ', ',') + '\n'
        file.write(text)

def get_xml(find): # 4
    with open('DZ7_tel_dict\\telbase.txt', mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        print('Фамилия Имя Телефон Описание')
        flag = False
        find = find.strip(" ,")
        for row in data:   
            if find.lower() in str(row).lower():
                xml.create(row)
                print(*row, '\nСоздан xml файл с контактом')
                flag = True
        if flag == False:
            print('Нет записи с такими данными')


def remove_one(find): # 5
    with open('DZ7_tel_dict\\telbase.txt', mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        li = []
        flag = False
        find = find.strip(" ,")
        find = find.replace('  ', ' ').split() 
        for row in data:   
            if len(find) == 2:
                if find[0].lower() in str(row[0]).lower() and find[1].lower() in str(row[1]).lower():
                    flag = True
                else:
                    li.append(row)
            elif len(find) == 1:
                if find[0].lower() in str(row).lower():
                    flag = True
                else:
                    li.append(row)
                  
    if flag == True:
        with open('DZ7_tel_dict\\telbase.txt', mode="w", encoding='utf-8') as file:
            data = csv.writer(file, delimiter = ",", lineterminator="\r")
            for row in li:
                data.writerow(row)
        print('Контакт удален')
    else: 
        print('Нет записи с такими данными')

def remove_all():  # 6
    with open('DZ7_tel_dict\\telbase.txt', mode="w", encoding='utf-8') as file:
        data = csv.writer(file, delimiter = ",", lineterminator="\r")
        data.writerow(['Фамилия', 'Имя', 'Телефон', 'Описание'])
        print('Фамилия Имя Телефон Описание\nЗаписей нет.')

def import_base(): # 7
    li_imp = []
    li_base = []
    with open('DZ7_tel_dict\\import_telbase.txt', mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        for row in data:
            li_imp.append(row)
        print(li_imp)
    with open('DZ7_tel_dict\\telbase.txt', mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')
        for row in data:
            li_base.append(row)

    for row in li_imp:
        if not str(row).lower() in str(li_base).lower():
            li_base.append(row)

    with open('DZ7_tel_dict\\telbase.txt', mode="w", encoding='utf-8') as file:
        data = csv.writer(file, delimiter = ",", lineterminator="\r")
        for row in li_base:
            data.writerow(row)
    print('Контакты импортированы.')