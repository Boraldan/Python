# 3. Напишите программу, которая принимает на вход число и проверяет,
#  кратно ли оно 5 и 10 или 15, но не 30.


n = int(input('Enter N: '))
if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print('yes')
else:
    print('no')
