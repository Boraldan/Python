# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('введите значение Х: 0 или 1 : '))
# y = int(input('введите значение Y: 0 или 1 : '))
# z = int(input('введите значение Z: 0 или 1 : '))

# if (not(bool(x + y + z))) == (not(bool(x))) * (not(bool(y))) * (not(bool(z))):
#     print("Выражение истинно")
# else:
#     print("выражение ложно")




# X, Y, Z = (input('Введите X: ')), (input('Введите Y: ')), (input('Введите Z: '))
# if not (X or Y or Z) == (not X) and (not Y) and (not Z):
#     print('True')
# else:
#     print('False')



for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(x, y, z, 'Утверждение истинно')
            else:
                print(x, y, z, '"Утверждение ложно')
