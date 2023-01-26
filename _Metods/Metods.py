
import os  #  очистка consol
os.system('cls||clear')

# ---------------
original = 2345                #   инвертируем число 2345 в 5432
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //=10
print(inverted) # 32

#  задать списко вручную --------------------

def get_numbers(num):              
    my_list = []
    for i in range(num):
        my_list.append(int(input('Введите число: ')))
    return my_list

#  задать списко произвольный нужного размера --------------------
def get_arr(num):              
    my_L = []
    for i in range(num):
        my_L.append(random.randint(1,11))
    return my_L

# функции работы со списком  -----------------------

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


#  задаем округление float--------------------------

str = '6.759104'
number = float(str)
result = '{:.4f}'.format(number)
print(result)


# Проверка ввода на число int ---------------
def check_int():
    num = input('введите число  = ')
    while not num.isdigit():
        num = input("Введите верное число = ")
    return int(num)
print(check_int())

\
while not (num.isdigit() or num[0] == '-' and  num[1:].isdigit()):

# str  операции  -----------------

st = 'x 1 g 2 w'
st = st.replace('x', '').replace('w', '') 

\
li = ' + '.join([f'{el}*x^{i+1}' for i, el in enumerate(myL[:-1]) if el != 0][::-1])

#  удаление символов по краям строки ----------------

str5 = '++++++Python Programming****** )$$$$$' 
str6 = str5. strip ( ' $*+)' ) 
print (str6) 

# создание словаря повторяющихся элементов в списке  ------ 

array = ["Bob", "Alex", "Bob", "John"]
result = {i: array.count(i) for i in array}
print(result)

# модуль подставляет время -------------------

from datetime import datetime as dt
time = dt.now().strftime('%H:%M:%S')
print(time)

#  преобразование строки в лист с комплексными числами ------------

st = '8 + 12j + 9'.split()
st = [int(el) if el.isdigit() else el for el in st]
st = [complex(el) if 'j' in str(el)  else el for el in st]
print(st)

#  добавление к list разными способами --------
new_list = []
my_tuple = (1,2,3,4,5)
my_list = [5,7,8,9,0]
my_tuple_new = (11,22,33)

new_list.extend(my_tuple)
print(new_list)
new_list += my_list
print(new_list)
new_list += 'wet'
print(new_list)
new_list.append(my_tuple)
print(new_list)

# присваивание значений переменным, если переменных не хватает --

my_tuple = (1,2,3,4,5)
my_list = [5,7,8,9,0]
my_tuple_new = (11,22,33)
my_list_new = [(11,22,33), (111,222,333), (1111,2222,3333)]
el_1, el_2, el_3 = my_tuple_new
print(el_1)
print(el_2)
print(el_3)

for el_1, el_2, el_3 in my_list_new:
    print(el_1, '----', el_2, '====', el_3)

el_1, el_2, *el_3 = my_tuple
print(el_1)
print(el_2)
print(el_3)
print()

#  считываем с файла TXTи записываем словари словарей{1 : { 1:2, 3:4}}   -- 

import csv   
di = {}
with open('for_import.txt', encoding='utf-8') as file:
    text = csv.reader(file, delimiter=',')   
    for i, row in enumerate(text, start=1):
        di[i] = dict(zip(row[1::2], row[2::2]))
# запись
st =''
li = []
for k in di:
    st += str(k) +','
    for k2, v in di[k].items():
        st += str(k2)+',' + str(v) + ','
    li.append(st.strip(","))
    st =''
with open('out_import.txt', mode="w", encoding='utf-8') as file:
    for el in li:
       file.write(el + '\n')

# ------------------------------------------