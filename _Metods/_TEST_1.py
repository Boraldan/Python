

path = "DZ4\\task_5\\file1.txt"
data = open(path, 'r')
for line in data:
    myL1 =  line
data.close()

path = "DZ4\\task_5\\file2.txt"
data = open(path, 'r')
for line in data:
    myL2 =  line
data.close()

print('Первый многочлен : ' + myL1)
print('Второй многочлен : ' + myL2)

myL1 = myL1.split( )
myL2 = myL2.split()


if 'x**' in myL1[0]:
    N = myL1[0].find('x') + 2
    t = myL1[0]       # выделяем отдельную переменную из списка
    n = int(t[N+1:])  # степень 
    A = int(t[:N-3])  # коофициент 

else:
    n = 1
    print(n)

while n > 1:
    for i1, el1 in enumerate(myL1):
        for i2, el2 in enumerate(myL2):
            if 'x**' + str(n) in el1 and 'x**' + str(n) in el2:
                    N1 = el1.find('x')
                    A1 = int(el1[:N1-1])  # коофициент 
                    N2 = el2.find('x')
                    A2 = int(el2[:N2-1])  # коофициент 
                    temp = str(A1+A2) + '*x**' + str(n)
                    n = n - 1
                    myL1[i1] = temp
                    # print(temp)
            elif el1[-1:] == 'x' and el2[-1:] == 'x':
                    N1 = el1.find('x')
                    A1 = int(el1[:N1-1])  # коофициент 
                    N2 = el2.find('x')
                    A2 = int(el2[:N2-1])  # коофициент 
                    temp = str(A1+A2) + '*x'
                    myL1[i1] = temp
                    # print(temp)
            elif  (el1.isdigit() and int(el1) > 0) and (el2.isdigit() and int(el2) > 0) :
                    temp = int(el1) + int(el2)
                    myL1[i1] = str(temp)
                    # print(temp)


# myL1 = str(myL1)

print(myL1)

newL = ''

for el in myL1:
    newL += str(el) + ' '

print(newL)