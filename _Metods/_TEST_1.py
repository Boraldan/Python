import os
os.system('cls||clear')

li = [['_','_','_'], ['_','_','_'], ['_','_','_']]
# print(li)


x = 'X'
x0 = '0'
co = 1
while co < 10:
    if co%2:
        print('Ход игрока Х: ')     
        a = int(input('Введите строку: '))
        b = int(input('Введите столбец: '))
        li[a-1][b-1] = x
    else:
        print('Ход игрока 0: ')     
        a = int(input('Введите строку: '))
        b = int(input('Введите столбец: '))
        li[a-1][b-1] = x0
        
    for el in li:
        print(el[0] + ' | ' + el[1] + ' | ' + el[2])

    if '0' == li[0][0] == li[0][1] ==li[0][2] or '0' == li[1][0] == li[1][1] == li[1][2] or '0' == li[2][0] == li[2][1] == li[2][2]:
        print('\n Победил игрок 0\n __КОНЕЦ__')  # по строкам
        break
    elif '0' == li[0][0] == li[1][0] ==li[2][0] or '0' == li[0][1] == li[1][1] == li[2][1] or '0' == li[0][2] == li[1][2] == li[2][2]:
        print('\n Победил игрок 0\n __КОНЕЦ__')  #  по столбцам
        break
    elif '0' == li[0][0] == li[1][1] ==li[2][2] or '0' == li[0][2] == li[1][1] ==li[2][0]:
        print('\n Победил игрок 0\n __КОНЕЦ__')  #  по диагонали
        break
    elif 'X' == li[0][0] == li[0][1] ==li[0][2] or 'X' == li[1][0] == li[1][1] == li[1][2] or 'X' == li[2][0] == li[2][1] == li[2][2]:
        print('\n Победил игрок X\n __КОНЕЦ__')   # по строкам
        break
    elif 'X' == li[0][0] == li[1][0] ==li[2][0] or 'X' == li[0][1] == li[1][1] == li[2][1] or 'X' == li[0][2] == li[1][2] == li[2][2]:
        print('\n Победил игрок X\n __КОНЕЦ__')   #  по столбцам
        break
    elif 'X' == li[0][0] == li[1][1] ==li[2][2] or 'X' == li[0][2] == li[1][1] ==li[2][0]:
        print('\n Победил игрок X\n __КОНЕЦ__')  #  по диагонали
        break
    

    print('---------------------')
    co += 1




 