# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
#  эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = int(input('введите число x = '))
y = int(input('введите число y = '))

if x==0 or y==0:
    print('введите правильное число')
elif x > 0 and y > 0:
     print('Четверь 1')
elif x < 0 and y > 0:
     print('Четверь 2')
elif x < 0 and y < 0:
     print('Четверь 3')
elif x > 0 and y < 0:
     print('Четверь 4')
    