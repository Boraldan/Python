# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

d = int(input('введите число = '))

bi_L=[]

while d > 0:
    if  d%2 ==0:
        d = d//2
        bi_L.append(0)
    else:
        d = (d-1)//2
        bi_L.append(1)

print(list(reversed(bi_L)))
