# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('введите число = ')

if "." in num:
    size = len(num)-num.find('.')
    num = int(float(num)*(10**size))
    
num = int(num)
sum = 0
while num > 0:
    sum += num%10
    num = num//10
print(sum)



# number = input('Введите число дробное или больше 10: ')
# sumDigits = 0

# for item in number:
#     if item.isdigit():
#         sumDigits += int(item)
# print(sumDigits)
