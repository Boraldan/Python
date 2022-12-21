# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('введите число = '))

array = list(range(-N,N+1))

multi = 1

path = "DZ2\\file.txt"
data = open(path, 'r')
for line in data:
    multi *= array[int(line)]
data.close()

print(multi)
print(f'{array}')
 
 