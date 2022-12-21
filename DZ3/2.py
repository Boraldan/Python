#     Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import random

def get_list(num):              
    my_list = []
    for el in range(num):
        my_list.append(random.randint(1, 6))
    return my_list

def multiPara (in_list):
    in_list2 = []
    for i in range(len(in_list)//2):
        in_list2.append(in_list[i] * in_list[-(i)-1])
    if (len(in_list)%2) != 0:
        in_list2.append(in_list[len(in_list)//2]**2)
    return  in_list2

N = int(input('введите число = '))

new_list = get_list(N)

print(f'{new_list}')
print(f'{multiPara(new_list)}')
 