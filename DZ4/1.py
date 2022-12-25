#     Вычислить число c заданной точностью d
#     Пример:
#  при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


def RoundNum(num1, d1):
    num1 = round(num1, d1)
    return num1


def main():
    num = float(input('введите число = '))
    d = int(input('введите количество знаков после запятой от 1 до 10 = '))
    print(RoundNum(num, d))

if __name__ == "__main__":
	main()