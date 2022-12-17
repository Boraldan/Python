# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('введите число 1 = ')

size = len(num) 
num = float(num)

i = 1
if num < 1: 
    while i < size-1:
        num*=10
        i= i+1

num = int(num)
sum = 0
while num > 0:
    sum += num%10
    num = num//10
print(sum)