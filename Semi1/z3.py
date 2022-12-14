# 1. Напишите программу, которая будет на вход принимать 
# число N и выводить числа от -N до N
#  *Примеры:* 
#      - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
 

# a = int(input('введите число 1 = '))
# for num in range(-a, a+1):
#     print(num, end = ' ')

# a = int(input('введите число 1 = '))
# list = range(-a, a+1)
# print(*list)



# num = int(input("Введите число N: "))
# for number in range(-num, num+1):
#     print(number, end=', ')


# num = int(input('введите число 1 = '))
# my_list = range(-num, num + 1)
# print(list(my_list))


num = int(input('введите число 1 = '))
print(list(range(-num, num + 1)))