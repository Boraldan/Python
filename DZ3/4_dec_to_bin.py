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

temp = list(reversed(bi_L))

bi_num = ""
for el in temp:
    bi_num += str(el)

print(f'Двоичное число = {bi_num}')


#------------------------- ниже хорошее решение


i = int(input('Input decimal number and I will convert it to binary: '))

string = ''
while i != 0:
    left = i % 2
    string = str(left) + string 
    i //= 2
print(f'This is a binary number: {string}')
