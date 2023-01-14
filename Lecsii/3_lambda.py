sum = lambda x: x+10
mult = lambda x: x*2

h = lambda f, g, x: f(g(x))
print(h(sum, mult, 5))

# тоже самое ^

h = lambda f, g, x: f(g(x))
print(h(lambda x: x+10, lambda x: x*2, 7))


\

def new(fi, b):
    return  fi(b)
def ino(aa):
    return aa + 1
print(new(ino, 5))

\

# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

f = open('f.txt', 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []

for e in numbers:
    if not e % 2:
        out.append((e,e **2))

print(out)

# тоже решение только без файла

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))

# тоже с использование map  и filter

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)

# ----------------------------------
# Проходили map, filter, zip, enumerate в Уроке 3
