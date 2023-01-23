import os  #  очистка consol
os.system('cls||clear')
# ---------------------------
import csv

def remove_one(find): # 5
    with open('telbase.txt', mode="r", encoding='utf-8') as file:   
        data = csv.reader(file, delimiter=',')   
        li = []
        flag = False
        find = find.strip(" ,")
        find = find.replace('  ', ' ').split() 
        for row in data:   
            if len(find) == 2:
                if find[0].lower() in str(row[0]).lower() and find[1].lower() in str(row[1]).lower():
                    flag = True
                else:
                    li.append(row)
            elif len(find) == 1:
                if find[0].lower() in str(row).lower():
                    flag = True
                else:
                    li.append(row)
                    
    if flag == True:
        with open('telbase.txt', mode="w", encoding='utf-8') as file:
            data = csv.writer(file, delimiter = ",", lineterminator="\r")
            for row in li:
                data.writerow(row)
        print('Контакт удален')
    else: 
        print('Нет записи с такими данными')


