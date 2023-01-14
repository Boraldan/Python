# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

f = open('semi5\\f1.txt', 'r')
data = f.read().split()
f.close()

data = list(map(int, data))

print(data)

for i, el in enumerate(data[:-1]):
    if el != data[i+1] - 1:
        print(data[i+1] - 1 )

\

n = [1,2,3,4,5,6,8,9]
print(*[val + 1 for i, val in enumerate(n[:-1]) if val != n[i+1] - 1])
