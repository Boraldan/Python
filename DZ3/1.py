#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
#   стоящих на нечётной позиции.
#     Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def get_list(num):              
    my_list = []
    for el in range(num):
        my_list.append(random.randint(0, 10))
    return my_list

def sum_od (in_list):
    sum = 0
    for i in range(1, len(in_list), 2):
        sum += int(in_list[i])
    return sum

N = int(input('введите число = '))

new_list = get_list(N)

print(f'{new_list}')
print(sum_od(new_list))