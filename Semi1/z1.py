# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
#     *Примеры:* 
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

a = int(input('введите число 1 = '))
b = int(input('введите число 2 = '))

if a*a == b or b*b == a:
    print('yes')
else:
    print('no')