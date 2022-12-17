# Реализуйте алгоритм перемешивания списка

import random

N = int(input('введите размер списка = '))

list = list(range(0,N))

for el in range(0,N):
    i = random.randint(0, N-1)
    temp1 = list[i] 
    j = random.randint(0, N-1)
    temp2 = list[j]
    list[i] = temp2
    list[j] = temp1

print(f"{list}")

 