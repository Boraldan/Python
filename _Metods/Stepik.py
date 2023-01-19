# Различные варианты решения одной задачи:

# Поиск MIN в введеных числах -----------

n = [int(input()) for _ in range(2)]
print(min(n))

\
a = [int(input()), int(input()), int(input()), int(input())]
a.sort()
print(a[0])

\
a1 = int(input())
a2 = int(input())
print(a1 if a1 < a2 else a2 )

\
print(sorted([int(input()), int(input())])[0])

\
print(min(int(input()) for _ in range(3)))

# Выбор из диапазона по заданому числу ----------------

a = int(input())
if  13 >= a:
    print('детство')
elif 14 <= a <=24:
    print('молодость')
elif 25 <= a <= 59:
    print('зрелость')
elif 60 <= a:
    print('старость')

\
a = int(input())
print(['детство', 'молодость', 'зрелость', 'старость'][sorted([13, 24, 59, a]).index(a)])

\
a = int(input())
v1, v2, v3, v4 = a <= 13, 14 <= a <= 24, 25 <= a <= 59, 60 <= a
print(v1 * 'детство' + v2 * 'молодость' + v3 * 'зрелость' + v4 * 'старость')

\
age = int(input())
print(("детство","молодость","зрелость","старость")[(14<=age<=24) + 2*(25<=age<=59) + 3*(age>=60)])

# сумма положительных цифр введеных  -------------------------

sum = 0
n =[int(input()) for i in range(3)]
for el in n:
    if el > 0:
        sum += el
print(sum)

\
print(sum([i for i in [int(input()) for _ in 'abc'] if i > 0]))

# проверка вхождение в диапазон  --------------------------------

num = int(input())
if -30 < num <=2 or 7 < num <= 25:    
    print('Принадлежит')
else:
    print('Не принадлежит')

\
print('Принадлежит' if int(input()) in (list(range(-29, -1)) + list(range(8, 26))) else 'Не принадлежит')

\
a = int(input())
print('Принадлежит' if (-30 < a <= -2) or (7 < a <= 25) else 'Не принадлежит')

\
n = int(input())
print("YES" if((n % 7 == 0 or n % 17 == 0) and 1000 <= n <= 9999) else 'NO')

#  Високосный год  ---------------------------------

a = int(input())
if (a%4 == 0 and a%100 != 0) or a%400 == 0:  
    print('YES') 
else:
    print('NO')

# Каскадный IF  --------------------------

a, b = int(input()), int(input())
if a > b:
    print("NO")
elif a < b:
    print("YES")
else:
    print("Don't know")

\
n, k = int(input()), int(input())
print("Don't know" if n == k else "YES" if n < k else "NO")

\
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b != c or a != b == c or a == c != b:
    print('Равнобедренный')
else:
    print('Разносторонний')

\
nums = set(int(input()) for _ in range(3))
print(["Равносторонний", "Равнобедренный", "Разносторонний"][len(nums) - 1])

# Среднее число из трех --------------------

a, b, c = int(input()), int(input()), int(input())
if a < b < c or c < b < a:
    print(b)
elif b < a < c or c < a < b:
    print(a)
else:
    print(c)

\
a, b, c = int(input()), int(input()), int(input())
print(a + b + c - min(a, b, c) - max(a, b, c))

# сортировка по цвету --------------------

b = [input() for i in range(2)]
b.sort()
if b == ['красный', 'синий']:
    print('фиолетовый')
elif b == ['желтый','синий']:
    print('зеленый')
elif b == ['желтый', 'красный']:
    print('оранжевый')
else:
    print('ошибка цвета')

\

mc = {'красный':1, 'синий':10, 'желтый': 100}
ac = {11:'фиолетовый', 101:'оранжевый', 110:'зеленый'}
c1, c2 = input(), input()
if c1 not in mc or c2 not in mc:
    print('ошибка цвета')
else:
    print(ac[mc[c1]+mc[c2]])

\
b = [input() for i in range(2)]
b.sort()
if b == ['красный', 'синий']:
    print('фиолетовый')
elif b == ['желтый','синий']:
    print('зеленый')
elif b == ['желтый', 'красный']:
    print('оранжевый')
else:
    print('ошибка цвета')

# рулетка казино и выбор цвета по номеру -----------------------

a = int(input())

if  a < 0 or a > 36:
    print('ошибка ввода')
elif   1 <= a <= 10 or 19 <= a <= 28 :
    if a%2 != 0:
        print('красный')
    else: 
        print('черный')
elif   11 <= a <= 18 or 29 <= a <= 36:
    if a%2 == 0:
        print('красный')
    else: 
        print('черный')
else:
    print('зеленый')

\
n = int(input())
print((['зеленый'] + 
       ['красный','черный'] * 5 +
       ['черный','красный'] * 4 + 
       ['красный','черный'] * 5 +
       ['черный','красный'] * 4) [n] if 0 <= n <= 36 else 'ошибка ввода')

\
n = int(input())
print('ошибка ввода' if not 0 <= n < 37 else 'зеленый' if n == 0 else ['черный','красный'][n%2 == (1<=n<=10 or 19 <=n<=28)])

# Пересечение двух отрезков ----------------------

a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())
a3 = max(a1,a2)
b3 = min(b1,b2)
if a3 < b3 :
    print(a3,b3)
elif a3 == b3 :
    print(a3)
else:
    print('пустое множество')
\

# Отделение числа после запятой float -----------

a = float(input())
print(int(a*10)%10)

\
n = float(input())
print(int((n - int(n))*100))

\
num = input()
dot = num.index('.')
print(num[dot+1])

# отделение дробной части float -------------------

print('0.' + input().split('.')[1])

\
a = float(input ())
print(a - a // 1)

\
n = float(input())
print(n % 1)

\
n = float(input())
print(n - int(n))

# разбиваем число и сравниваем цифры между собой ------ 

a = int(input())
s = a//100 
f = a%10
m = (a%100)//10
t = (s, f, m)
if (s + f + m) - (min(t)+ max(t)) == max(t) - min(t):
    print('Число интересное')
else:
    print('Число неинтересное')
 
\
x = list(input())
print('Число интересное' if int(max(x)) - int(min(x)) == int(sorted(x)[1]) else 'Число неинтересное')

\
n = sorted([int(i) for i in list(input())])
print('Число интересное' if n[2]-n[0]==n[1] else 'Число неинтересное')

# sum введенных элементов -------------------
n = ([abs(float(input())) for _ in range(5)])
sum = 0
for el in n:
    sum += el
print(sum)

\
print(sum([abs(float(input())) for _ in range(5)]))

# сравниваем короткое и длинное слово -----------
st = ([input() for _ in range(3)])

mi = len(st[0])
ma = len(st[0])
ima = st[0]
im = st[0]

for el in st:
    if ma < len(el):
        ma = len(el)
        ima = el
    if mi > len(el):
        mi = len(el)
        im = el

print(im)
print(ima)

\

print(*sorted([input() for i in range(3)], key=len)[0::2], sep='\n')

# арифметическая прогрессия в словах --------------------

st = (sorted([len(input()) for _ in range(3)]))
if st[1] - st[0] == st[2] - st[1]:
    print('YES')
else:
    print('NO')

\
a, b, c = len(input()), len(input()), len(input())
if (a + b + c) % 3 == 0:
    print('YES')
else:
    print('NO')

# ипорт модуля math  или его компонентов ---------------

from math import pi
print(pi * (r := float(input())) ** 2, 2 * pi * r, sep='\n')

# for и без него  -------------------

st = input() 
n = int(input())
for _ in range(n):
    print(st)

\
s, n = input(), int(input())
print((s + '\n') * n)

\
print((input()+'\n')*int(input()))
\
print('AAA\n'*6 + 'BBBB\n'*5 + 'E\n' + 'TTTTT\n'*9 + 'G')

# переворачивание числа --------------

num = int(input())
res = 0
while num != 0:
    last_digit = num % 10
    res += last_digit * (10**(len(str(num))-1))
    # res = res*10 +last_digit                       или так
    num = num // 10
print(res)

\
print(input()[::-1])

# последовательность цифр в числе на убывание проверяем  54321 -----

num = int(input())
last = num%10
flag = True
num = num // 10
while num > 0:
    last2 = num%10
    if last > last2:
        flag = False
    last = last2
    num = num // 10
if flag == True:
    print('YES')
else:
     print('NO')

\
n = int(input())
while n % 10 <= n // 10 % 10:
    n //= 10
print('YES' if n < 10 else 'NO')

# ------------------------------