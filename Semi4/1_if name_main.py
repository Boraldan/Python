if __name__ == "__main__":
	main()


def check_num():
    num = input('введите число 1 = ')
    while not num.isdigit():
        num = input("Введите верное число = ")
    return int(num)

print(check_num())