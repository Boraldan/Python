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

max = 0
min = 1

for num in my_L:
    num = str(num)
    if "." in num:
        size = num.find('.')
        d = len(num)-num.find('.') - 1
        N = float(num[size+1:]) / 10**d
    
    if N > max:
        max = N
    if N < min:
        min = N


print(f'Разница между {max} - {min}  = {round(max - min, 2)}')




