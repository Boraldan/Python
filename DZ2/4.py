# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('введите число = '))

array = list(range(-N,N+1))

path = "DZ2\\file.txt"
data = open(path, 'r')
for line in data:
    my_i = int(line)    
data.close()

multi = 1

while my_i > 0:
    i = my_i%10
    multi *= array[i-1]
    my_i = my_i//10

print(multi)
print(*array)
 