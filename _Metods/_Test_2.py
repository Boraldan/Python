import random

k = int(input('Введите значение натуральной степени k: '))
myL = [random.randint(0, 5) for i in range(k + 1)]
print(myL)


li = ' + '.join([f'{el}*x^{i+1}' for i, el in enumerate(myL[:-1]) if el != 0][::-1])
print(li)
if int(li[-1]) == 1:
    li = li[:-2]
li = li + ' + ' + str(random.randint(1, 100)) + ' = 0' 
print(li)
