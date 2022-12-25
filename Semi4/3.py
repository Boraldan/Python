# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python ( с помощью модуля Sympy)

from math import sqrt

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите с: "))
x1 = 0
x2 = 0

disc = b**2 - 4*a*c
print(sqrt(disc))
if disc < 0:
    print("Корней нет.")
elif disc == 1:
    x1 = -b/(2*a)
    print(x1)
elif disc > 0:
    x1 = (-b - sqrt(disc))/(2*a)
    x2 = (-b + sqrt(disc))/(2*a)
    print(x1,x2)
