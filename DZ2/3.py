# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#     Пример:- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import math

N = int(input('введите число = '))

list = []
sum = 0
for i in range(1,N+1):
   list.append(int(round((1 + 1/i)**i, 0)))
   sum +=int(round((1 + 1/i)**i, 0))

print(list)
print(sum)
