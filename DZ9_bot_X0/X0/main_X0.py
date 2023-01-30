# Здравствуйте, придумайте что можно добавить или изменить в проекте, с использованием сторонних библиотек. 
# Например, цветной текст в консоли, или создать не в консоли, а интерфейс с помощью tkinter, либо еще с
#  использованием какой нибудь библиотеки. Только еще главное использовать виртуальное окружение и в нем 
#  устанавливать эту библиотеку и проекту сгенерировать файл requirements.txt

import os
os.system('cls||clear')

import emoji 

def game(li):
    x = 'X'
    x0 = '0'
    count = 1
    
    def check(x, y, L):
        while L[x-1][y-1] != '_':
            print(emoji.emojize('ЭТА ЯЧЕЙКА ЗАНЯТА :clown_face: ----> Введите верную ячейку: '))     
            x = int(input('Введите строку: '))
            y = int(input('Введите столбец: '))
        return x, y

    while count < 10:
        if count % 2:
            print(emoji.emojize('Ход игрока :cross_mark: : '))     
            a = int(input('Введите строку: '))
            b = int(input('Введите столбец: '))
            a, b = check(a, b, li)
            li[a-1][b-1] = x
        else:
            print(emoji.emojize('Ход игрока :hollow_red_circle: : '))     
            a = int(input('Введите строку: '))
            b = int(input('Введите столбец: '))
            a, b = check(a, b, li)
            li[a-1][b-1] = x0
            
        for el in li:
            print(el[0] + ' | ' + el[1] + ' | ' + el[2])

        if '0' == li[0][0] == li[0][1] ==li[0][2] or '0' == li[1][0] == li[1][1] == li[1][2] or '0' == li[2][0] == li[2][1] == li[2][2]:
            print(emoji.emojize('\n Победил игрок 0  :thumbs_up: 	:1st_place_medal:\n __КОНЕЦ__'))  # по строкам
            break
        elif '0' == li[0][0] == li[1][0] ==li[2][0] or '0' == li[0][1] == li[1][1] == li[2][1] or '0' == li[0][2] == li[1][2] == li[2][2]:
            print(emoji.emojize('\n Победил игрок 0 :thumbs_up: 	:1st_place_medal:\n __КОНЕЦ__'))  #  по столбцам
            break
        elif '0' == li[0][0] == li[1][1] ==li[2][2] or '0' == li[0][2] == li[1][1] ==li[2][0]:
            print(emoji.emojize('\n Победил игрок 0 :thumbs_up: 	:1st_place_medal:\n __КОНЕЦ__'))  #  по диагонали
            break
        elif 'X' == li[0][0] == li[0][1] ==li[0][2] or 'X' == li[1][0] == li[1][1] == li[1][2] or 'X' == li[2][0] == li[2][1] == li[2][2]:
            print(emoji.emojize('\n Победил игрок X :thumbs_up: 	:1st_place_medal:\n __КОНЕЦ__'))   # по строкам
            break
        elif 'X' == li[0][0] == li[1][0] ==li[2][0] or 'X' == li[0][1] == li[1][1] == li[2][1] or 'X' == li[0][2] == li[1][2] == li[2][2]:
            print(emoji.emojize('\n Победил игрок X :thumbs_up: 	:1st_place_medal:\n __КОНЕЦ__'))   #  по столбцам
            break
        elif 'X' == li[0][0] == li[1][1] ==li[2][2] or 'X' == li[0][2] == li[1][1] ==li[2][0]:
            print(emoji.emojize('\n Победил игрок X :thumbs_up: 	:1st_place_medal:\n __КОНЕЦ__'))  #  по диагонали
            break
                
        count += 1
        if count == 10:
            print('-------- НИЧЬЯ ---------')
        else:
            print('-----------------------')        


def main():

    my_li = [['_','_','_'], ['_','_','_'], ['_','_','_']]
    for el in my_li:
            print(el[0] + ' | ' + el[1] + ' | ' + el[2])
    game(my_li)
    

if __name__ == "__main__":
	main()