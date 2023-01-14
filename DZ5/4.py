# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def zip_st(st):
    co = 1
    res = ''
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            co += 1
            if i + 2 == len(st):
                res += str(co) + st[i]
        elif i + 2 == len(st):
                res += str(co) + st[i]
                res += '1' + st[i+1]
        else:
            res += str(co) + st[i] + ' '
            co = 1
    print(res)
    return res

def unpack(res_in):
    li = res_in.split()
    res_n = ''
    for el in li:
        res_n += str(el[-1]) * int(el[:-1])
    print(res_n)
    return res_n

def main():
    my_st = 'aaaa1aaavvvvvvvvvvvveeeeeeeeeefrrrrooooo1ww'
    print(my_st)
    my_st = zip_st(my_st)
    my_st = unpack(my_st)


if __name__ == "__main__":
	main()