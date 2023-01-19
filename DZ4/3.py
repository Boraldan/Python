# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

import random

def get_arr(num):              
    my_L = []
    for i in range(num):
        my_L.append(random.randint(1,10))
    return my_L

def del_el (in_L):
    temp = []
    i = 0
    while i < len(in_L)-1:
        if in_L[i] in in_L[i+1:]:
            temp.append(in_L[i])
        i=i+1
    return (list(set(in_L) - set(temp)))

def main():
    number = int(input('введите размер списка '))
    arr = get_arr(number)
    print(arr) 
    print(del_el(arr))
     

if __name__ == "__main__":
	main()

# другой вариант решения задачи


res = [random.randint(1, 7) for i in range(10)]
print('Создаем список: ', res, '\n')

res_1 = list(filter(lambda x: res.count(x) == 1, res))
res_2 = [i for i in res if res.count(i) == 1]
res_3 = list(set(res))

print('Список уникальных элементов: ', res_1)
print('Список уникальных элементов: ', res_2)
print('Список уникальных элементов: ', res_3, '\n')
