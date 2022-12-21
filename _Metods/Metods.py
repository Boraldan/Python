original = 2345                   инвертируем число 2345 в 5432
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //=10
print(inverted) # 32


def get_numbers(num):              
    my_list = []
    for i in range(num):
        my_list.append(int(input('Введите число: ')))
    return my_list
    
my_list = get_numbers(3)


colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
colors.append('gray') # добавить в конец
colors.remove('red') 
del colors[0] # удалить элемент   


# перевод из строки в число и суммирование ---------------------

number = input('Введите число дробное или больше 10: ')
sumDigits = 0

for item in number:
    if item.isdigit():
        sumDigits += int(item)
print(sumDigits)


# --------------------------