# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81


import random

# num = int(input('введите число 1 = '))
# i = 0 
# while i < num:
#     print(random.randint(0, 125), end=', ')
#     i=i+1

 
num = int(input('введите число 1 = '))
list = [] 
i = 0 
while i < num:
    list.append(random.randint(0, 125))
    i=i+1

print(*list)