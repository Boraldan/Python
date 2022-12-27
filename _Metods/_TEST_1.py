path = "DZ4\\task_5\\file1.txt"
data = open(path, 'r')
for line in data:
    max =  line
data.close()

path = "DZ4\\task_5\\file2.txt"
data = open(path, 'r')
for line in data:
    min =  line
data.close()

print('Первый многочлен : ' + max)
print('Второй многочлен : ' + min)

max = max.split()
min = min.split()

if len(max) > len(min):
    max = max
    min = min
else:
    max = min
    min = max


if 'x**' in max[0]:
    N = max[0].find('x') + 2
    t = max[0]       # выделяем отдельную переменную из списка
    n = int(t[N+1:])  # степень 
    # A = int(t[:N-3])  # коофициент 

else:
    n = 1
    print(n)

count1 = 0
count2 = 0

while n > 0:
    for i1, el1 in enumerate(max):
        for i2, el2 in enumerate(min):
            if 'x**' + str(n) in el1 and 'x**' + str(n) in el2:
                    N1 = el1.find('x')
                    A1 = int(el1[:N1-1])  # коофициент 
                    N2 = el2.find('x')
                    A2 = int(el2[:N2-1]) 
                    max[i1] = str(A1+A2) + '*x**' + str(n)
            elif el1[-1:] == 'x' and el2[-1:] == 'x':
                    N1 = el1.find('x')
                    A1 = int(el1[:N1-1])  
                    N2 = el2.find('x')
                    A2 = int(el2[:N2-1])   
                    temp = str(A1+A2) + '*x'
                    if count1 == 0:
                        max[i1] = temp
                        count1 +=1
            elif  (el1.isdigit() and int(el1) > 0) and (el2.isdigit() and int(el2) > 0) :
                    temp = int(el1) + int(el2)
                    if count2 == 0:
                        max[i1] = str(temp)
                        count2 +=1
    n = n - 1



newL = ''

for el in max:
    newL += str(el) + ' '

print('Итоговый многочлен: ' + newL)

with open('DZ4\\task_5\\task5_file.txt', 'w') as data: 
    data.write(newL)

