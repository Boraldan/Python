# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.  fgdhfgdhaa  dfgdfa

import os  #  очистка consol
os.system('cls||clear')
# ---------------------------

def zip_st(st):
    count = 1
    res = ''
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            count += 1                
        else:
            res += str(count) + st[i] + ' '
            count = 1
    if st[i] == st[i+1]:
        res += str(count) + st[i]
    else:
        res += '1' + st[i + 1]

    print(res)
    return res

def unpack(res_in):
    li = res_in.split()
    res_n = ''
    for el in li:
        res_n +=  int(el[:-1]) * str(el[-1])
    print(res_n)
    return res_n

def main():
    st_in = 'aaaa1aaavvvvvggggggvvvVVvveeeeeeRe'

    with open('DZ5\\task4_in.txt', 'w') as data:   # закроет соединение автоматически с файлом
        data.write(st_in)
    with open('DZ5\\task4_in.txt', 'r') as data:    
        my_st = data.readline()
    print(my_st)
    my_st = zip_st(my_st)
    with open('DZ5\\task4_zip.txt', 'w') as data:   
        data.write(my_st)
    with open('DZ5\\task4_zip.txt', 'r') as data:    
        my_st = data.readline()
    my_st = unpack(my_st)
    with open('DZ5\\task4_unpack.txt', 'w') as data:   
        data.write(my_st)

if __name__ == "__main__":
	main()