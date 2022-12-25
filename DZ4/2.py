# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def finds(num):
    my_l = []
    i = 2
    t = num  
    while i * i <= num:
            if num % i == 0:
                my_l.append(i)
                num//=i
            else:
                i += 1
    my_l.append(num)  
    my_l = set(my_l)
    print('{} = {}' .format(t, my_l))  


def main():
    num1 = int(input("Введите число = "))
    finds(num1)

if __name__ == "__main__":
	main()