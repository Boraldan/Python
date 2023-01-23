# Применяем map 
# 
# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
#     Пример:
#  [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
#     Пример:
#  [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

# leng = int(input('введите размер списка = '))

# my_L = []

# for i in range(leng):
#     my_L.append((float(random.randint(100, 999))/100))
# print(my_L)

# max = 0  #   искать 
# min = 1

# for num in my_L:
#     num = str(num)
#     if "." in num:
#         index_point = num.find('.')
#         # d = len(num)-num.find('.') - 1
#         # N = float(num[index_point+1:]) / 10**d
#         N = float(num[index_point:])
    
#     if N > max:
#         max = N
#     if N < min:
#         min = N
# print(f'Разница между {max} - {min}  = {max - min}')



leng = int(input('введите размер списка = '))
my_L = [float(random.randint(100, 999))/100 for _ in range(leng)]
print(my_L)

my_L = list(map(lambda x: x%1, my_L))
print(f'Разница между {round(max(my_L), 2)} - {round(min(my_L), 2)}  = {round(max(my_L) - min(my_L), 2)}')