# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('введите число = ')

if "." in num:
    size = len(num)-num.find('.')
    num = float(num)
    i = 1
    while i < size:
            num*=10
            i= i+1

num = int(num)
sum = 0
while num > 0:
    sum += num%10
    num = num//10
print(sum)