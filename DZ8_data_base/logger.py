import csv  

def get_students():
    di = {} 
    with open('DZ8_data_base\\students.txt', encoding='utf-8') as file:
        text = csv.reader(file, delimiter=',')   
        for row in text:
            di[int(row[0])] = [el for el in row[1:]]
    return di

def get_class():
    di = {} 
    with open('DZ8_data_base\\classes.txt', encoding='utf-8') as file:
        text = csv.reader(file, delimiter=',')   
        for row in text:
            di[row[0]] = [el for el in row[1:]]
    return di

def set_students(di):
    li = []
    for key in  di:
        st =''
        st += str(key) +',' + ','.join(di[key])
        li.append(st)
        st =''
    with open('DZ8_data_base\\students.txt', mode="w", encoding='utf-8') as file:
        for el in li:
            file.write(el + '\n')

def set_classes(di):
    li = []
    for key in  di:
        st =''
        st += key +',' + ','.join(di[key])
        st = st.strip(" ,")
        li.append(st)
        st =''
    with open('DZ8_data_base\\classes.txt', mode="w", encoding='utf-8') as file:
        for el in li:
            file.write(el + '\n')

def print_data(di):
    print(f'id       Фамилия  Имя  Отчество  Дата   рождения  Телефон  Класс')
    for key in di:
        print(key, '->', *di[key], sep='   ')

def print_class(di):
    print(f'id_классов   id_студентов')
    for key in di:
        print(key, '->', *di[key], sep='   ')