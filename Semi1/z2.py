# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


# max = 0

# for _ in range(5): # i = 0,1,2,3,4
#     num = int(input("Введите число: "))
#     if num > max:
#         max = num
# print(max)



list = (-1, 4, 118, 7, 8)

max = list[0]
for i in  list:
    if i > max:
        max = i
print(max)


# list = (-1, 4, 118, 7, 8)

# max = list[0]
# for i in  range(1,len(list)):
#     if list[i] > max:
#         max = list[i]
# print(max)


# list = (-1, 4, 118, 7, 8)

# max = list[0]
# for num in  list[1:]:
#     if num > max:
#         max = num
# print(max)




# def get_numbers(num): 
#     list = []
#     max = 0
#     for i in range(num):
#         num = int(input('Введите число: '))
#         list.append(num)
#         if num > max:
#             max = num
#     return list, max
    

# # def find_max(list):
# #     max = list[0]
# #     for i in list:
# #         if i>max:
# #             max = i
# #     return max

# my_list, num_max = get_numbers(5)
# print(mylist)
# print(num_max)
