# Реализуйте алгоритм перемешивания списка

import random

N = int(input('введите размер списка = '))

list = list(range(0,N))

for el in range(0,N):
    i = random.randint(0, N-1)
    j = random.randint(0, N-1)
    list[i], list[j] = list[j], list[i]

print(f"{list}")

 