import os  #  очистка consol
os.system('cls||clear')
# ---------------------------

import csv   

my_dir = {}

# with open('for_import.csv', encoding='utf-8') as file:
#     text = [str(el).split(';') for el in file.readlines()]
# # text[0][0] = 1
# for i in range(len(text)):
#     my_dir[int(text[i][0])] = dict(zip(text[i][1::2], text[i][2::2]))
# print(text)
# print(my_dir)


with open('for_import.txt', encoding='utf-8') as file:
    text = csv.reader(file, delimiter=',')   
    # text = file.readlines()
    # text = file.read()
    # print(text)

    # with open('for_import.txt', 'w', encoding='utf-8') as file:

    for i, row in enumerate(text, start=1):
        my_dir[i] = dict(zip(row[1::2], row[2::2]))

for key in my_dir.keys():
    print(str(key) + ' - ', end='')
    print(*my_dir[key].values())


# print(my_dir)