
from math import pi 



def RoundNum(num1, d1):
    num1 = round(num1, d1)
    return num1


def main():
    # num = float(input('введите число = '))
    d = int(input('введите количество знаков после запятой от 1 до 10 = '))
    print(RoundNum(pi, d))

if __name__ == "__main__":
	main()