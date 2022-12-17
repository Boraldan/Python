# 3. Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.



# str1 = input()
# str2 = input()
# N = str1.count(str2)
# print(N)
 

# str1 = 'sjhhakhfsjhfishpafhsisjh'
# str2 = 'sjh'
# cont= 0
# for i in range(len(str1)):
#     if str2[0] == str1[i] and  str2[1] == str1[i+1] and str2[2] == str1[i+2]:
#        cont= cont + 1

# print(cont)


str1 = 'sjhhakhfsjhfishpafhsisjh'
str2 = 'sjh'

counter = 0
for i in range(len(str1)):
    if str2 == str1[i: i + len(str2)]:
        counter += 1
            
print(f'Вторая строка встречается в первой {counter} раз')
