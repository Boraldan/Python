# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# list(map(int,input().split()))

# my_list = input('Введите числа через пробел: ').split()
# print(my_list)
# num = list(map(len, my_list))

# print(num)

# num2 = [int(num) for num in input().split()]

# print(num2)


num = input('введите размер списка = ').split()

my_L = []
for el in num:
    my_L.append(int(el))
    
print(my_L)
print(f" Мах =  {(max(my_L))},   Min = {(min(my_L))}")