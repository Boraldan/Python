# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90
 
list = [-1, 4, 118, 7, 800]  # 1 вариант
max = list[0]
for el in list[1:]:
    if el > max:
        max = el
print(max)


# list = [-1, 4, 118, 7, 8]
# max = list[0]
# for i in  range(1,len(list)):
#     if list[i] > max:
#         max = list[i]
# print(max)
