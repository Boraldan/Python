# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


path = "DZ4\\task_5\\file1.txt"
data = open(path, 'r')
for line in data:
    mno1 =  line
data.close()

path = "DZ4\\task_5\\file2.txt"
data = open(path, 'r')
for line in data:
    mno2 =  line
data.close()

mnogo = mno1[:-4] + " + " + mno2

with open('DZ4\\task_5\\task5_file.txt', 'w') as data: 
    data.write(mnogo)