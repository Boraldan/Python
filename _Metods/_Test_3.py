import os  #  очистка consol
os.system('cls||clear')
# ---------------------------

import csv

di ={}
li = (1, 2)
li2 = ('Имя', 'Класс')
di[1] = dict(zip(li, li2))
print(di)
di[1].update({17 : 77 })
print(di)
 

book = {1 : {'Apple': 'In stock', 'Pear': 'In stock', 'Peach': 'In stock', 'Banana': 'In stock'},\
        2 : {'Apple': 'In stock', 'Pear': 'In stock', 'Peach': 'In stock', 'Banana': 'In stock'}}


# for key in book.keys():
#     print(key,' - ', *book[key].values())

st =''
li = []
for k in book:
    st += str(k) +','
    for k2, v in book[k].items():
        st += str(k2)+',' + str(v) + ','
        # print(k2, v, end=', ')
    li.append(st.strip(","))
    st =''


with open('out_import.txt', mode="w", encoding='utf-8') as file:
    file.write
    for el in li:
       file.write(el + '\n')

print(li)