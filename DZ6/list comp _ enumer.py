# Задача измененная с использованием enumerate, list comprehension
# 
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#      (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#     Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

# def K_str(k):
#     mn = ""
#     for el in range(k, 0, -1):
#         A = random.randint(0,100)
#         if A != 0:
#             if el ==1:
#                 mn = mn + " + " + str(A)+ "*x"
#             elif el == k:
#                 mn = mn +str(A)+ "*x**"+str(el)
#             else:
#                 mn = mn + " + " + str(A)+ "*x**"+str(el)
#     A = random.randint(0,100)
#     if A != 0:
#         mn = mn + " + " + str(A) + " = 0"
#     else:
#         mn = mn  + " = 0"
#     return mn

# def w_file(in_str):
#     with open('DZ4\\task4_file.txt', 'w') as data:   # закроет соединение автоматически с файлом
#         data.write(in_str)

# def main():
#     num = int(input('Введите степень К =  '))
#     my_K = K_str(num)
#     print(my_K)
#     w_file(my_K)


# if __name__ == "__main__":
# 	main()


k = int(input('Введите значение натуральной степени k: '))
myL = [random.randint(0, 5) for i in range(k + 1)]
print(myL)


li = ' + '.join([f'{el}*x^{i+1}' for i, el in enumerate(myL[:-1]) if el != 0][::-1])
print(li)
if int(li[-1]) == 1:
    li = li[:-2]
li = li + ' + ' + str(random.randint(1, 100)) + ' = 0' 
print(li)