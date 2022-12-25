# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
#     Пример:
#  [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

leng = int(input('введите размер списка = '))

my_L = []

for i in range(leng):
    my_L.append((float(random.randint(100, 999))/100))

print(my_L)

max = 0  #   искать 
min = 1

for num in my_L:
    num = str(num)
    if "." in num:
        index_point = num.find('.')
        # d = len(num)-num.find('.') - 1
        # N = float(num[index_point+1:]) / 10**d
        N = float(num[index_point:])
    
    if N > max:
        max = N
    if N < min:
        min = N


print(f'Разница между {max} - {min}  = {max - min}')





# -------------------------------------

# import random
# from random import randint
# import os
# os.system('cls')


# s = []
# s1 = []
# for i in range(randint(2, 10)):
#     num = random.uniform(0, 10)
#     s.append(round(num, 2))
#     num1 = s[i] % 1
#     s1.append(round(num1, 2))

# print("Случайно заданный список из вещественных чисел : ")
# print()

# print(s)
# print(s1)
# print()
# res = max(s1) - min(s1)
# print("Разница между максимальным и минимальным значением дробной части : ", res)

