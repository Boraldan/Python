 

# проверка  верного ввода int (на числа с минусом учтена):
# while not (num.isdigit() or num[0] == '-' and  num[1:].isdegit()):
 
myL1 = ("5*x**5 + 9*x**4 + 7*x**3 + 7*x**2 + 3*x + 5 = 0").split()
myL2 = ("7*x**5 + 2*x**4 + 7*x**3 + 8*x**2 + 4*x + 3 = 0").split()

if 'x**' in myL1[0]:
    N = myL1[0].find('x') + 2
    t = myL1[0]       # выделяем отдельную переменную из списка
    n = int(t[N+1:])  # степень 
    A = int(t[:N-3])  # коофициент 
    # print(n)
    # print(A)
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
                    print(temp)

print(myL1)

        
    # if el1.isdigit() and int(el1) > 0:
    # el1.find('x**')
   


# print(myL1)