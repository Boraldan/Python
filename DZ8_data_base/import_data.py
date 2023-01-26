import logger as lr

def create_cl(name, classes):
    if not name in classes:
        name = input('''Введите номер нового класса: ''')
    classes[name] = []
    return name, classes

def create_student():
    students = lr.get_students()
    id_student = max(students.keys()) + 1
    classes = lr.get_class()
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    patro = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    class_name = input("Введите номер класса ученика: ")
    if class_name not in classes:
        print("Такого класса нет. ")
        class_name, classes = create_cl(class_name, classes)
    classes[class_name].append(str(id_student))
    st_data = [surname, name, patro, birth, tel, class_name]
    students[id_student] = st_data
    lr.print_data(students)
    lr.set_students(students)
    lr.set_classes(classes)

def edit_student():
    students = lr.get_students()
    student_id = int(input("Введите id студента."))
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    patro = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    class_name = students[student_id][-1]
    new_st_data = [surname, name, patro, birth, tel, class_name]
    students[student_id] = new_st_data
    lr.set_students(students)
    lr.print_data(students)

def delete_student():
    students = lr.get_students()
    classes = lr.get_class()
    id_student = int(input("Введите id студента:"))
    classes[students[id_student][-1]].remove(str(id_student))
    del students[id_student]
    lr.set_students(students)
    lr.set_classes(classes)

def change_class():
    students = lr.get_students()
    classes = lr.get_class()
    student_id = int(input("Введите id студента: "))
    old = students[student_id][-1]
    print(old)
    new = input("Введите номер класса куда переводят: ")

    if new not in classes:
        print("Такого класса нет. ")
        new, classes = create_cl(new, classes)

    classes[old].remove(str(student_id))
    classes[new].append(str(student_id))
    students[student_id].remove(old)
    students[student_id].append(new)
    lr.print_class(classes)
    lr.set_students(students)
    lr.set_classes(classes)

def view_one(find):
    di = lr.get_students()
    flag = False
    find = find.strip(" ,")
    find = find.replace('  ', ' ').split() 
    print(f'id       Фамилия  Имя  Отчество  Дата   рождения  Телефон  Класс')
    for key in di:   
        if len(find) == 2 and find[0].lower() in str(di[key][0]).lower() and find[1].lower() in str(di[key][1]).lower():
            print(key, '->', *di[key], sep='   ')
            flag = True
        elif len(find) == 1 and find[0].lower() in str(di[key]).lower():
            print(key, '->', *di[key], sep='   ')
            flag = True
    if flag == False:
        print('Нет записи с такими данными')