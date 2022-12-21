# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
sim = 'qwe'
a = 0

for i in range(len(my_list)):
    if sim == my_list[i]:
        a= a+1
        if a==2:
          print(i)
          break
else: 
    print("нету")


 