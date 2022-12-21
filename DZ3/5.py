#     Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

N = int(input('введите число = '))

Fib = [0, 1]
negaFib = [1]

for n in range(2, N+1):
    f = Fib[n-2] + Fib[n-1]
    Fib.append(f)
    if n%2 == 0:
        negaFib.insert(0, -(f))
    else:
        negaFib.insert(0, f)

FinFib = negaFib + Fib

print(f'{FinFib}')
