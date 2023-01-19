# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
#      2+2 => 4; 
#     1+2*3 => 7; 
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:* 
#         1+2*3 => 7; 
#         (1+2)*3 => 9;
 
# st = '2*3'
# num = ''
# li = []
# for el in st:
#     if  el.isdigit():
#         num += el
#     else:
#         li.append(int(num))
#         li.append(el)
#         num = ''      
# li.append(num)

# res=[]

# for i in range(1, len(li), 2):
#     if li[i] == '*':
#         res = li.pop(i-1) * li.pop(i+1) 
#         li[i-1] = res

# print(res)

s = '2+12*3'
num = ''
my_list = []
for elem in s:
    if elem.isdigit():
        num += elem
    else:
        my_list.append(int(num))
        my_list.append(elem)
        num = ''
my_list.append(int(num))

if '*' in my_list or '/' in my_list:
    for i in range(1, len(my_list), 2):
        if my_list[i] == '*':
            result = my_list.pop(i+1) * my_list.pop(i-1)
            my_list[i-1] = result
        elif my_list[i] == '/':
            result = my_list.pop(i+1) / my_list.pop(i-1)
            my_list[i-1] = result
            
if '+' in my_list or '-' in my_list:
    for i in range(1, len(my_list), 2):
        if my_list[i] == '-':
            result = my_list.pop(i+1) - my_list.pop(i-1)
            my_list[i-1] = result
        elif my_list[i] == '+':
            result = my_list.pop(i+1) + my_list.pop(i-1)
            my_list[i-1] = result

print(my_list)

\

