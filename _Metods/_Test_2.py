
import os, random
os.system('cls||clear')

def pvp(n, sp):
    re = 0
    co = 1
    while n > 0:
        if co%2 != 0:
            p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
            if 1 > p or p > sp:
                while re < 3:
                    print(f'Неверное число. Введите число от 1 до {sp}: ')     
                    p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
                    if 0 < p < sp + 1:
                        break
            n -= p
            if n <= 0:
                print('Победа первого игрока')
                break
            print(f'Осталось {n} конфет')
        else:
            p = int(input(f'Ход ВТОРОГО игрока. Введите число от 1 до {sp}: '))
            if 1 > p or p > sp:
                while re < 3:
                    print(f'Неверное число. Введите число от 1 до {sp}: ')     
                    p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
                    if 0 < p < sp + 1:
                        break
            n -= p
            if n <= 0:
                print('Победа второго игрока')
                break
            print(f'Осталось {n} конфет')
        co += 1

    print('------------Игра закончена----------------')

def PvComp(n, sp):  # Компьютер ходит первым
    
    pr_st = n % (sp + 1)
    re = 0
    co = 1
    start = 0
    f_start = n

    while n > 0:
        if co%2 != 0: #  первый ход компьютера
            p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
            if 1 > p or p > sp:
                while re < 3:
                    print(f'Неверное число. Введите число от 1 до {sp}: ')     
                    p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
                    if 0 < p < sp + 1:
                        break
            n -= p
            if n <= 0:
                print('Победа первого игрока')
                break
            print(f'Осталось {n} конфет')
        else:
            if n > f_start//2:
                temp = random.randint(1, sp+1)
                n -= temp
                print(f'Компьютер взял {temp}. Осталось {n} конфе')  
            elif p < pr_st and start == 0:
                start += 1
                n -= pr_st - p
                print(f'Компьютер взял {pr_st - p}. Осталось {n} конфе') 
            elif p > pr_st and start == 0:
                start += 1
                n -= pr_st + sp + 1 - p
                print(f'Компьютер взял {pr_st + sp + 1 - p}. Осталось {n} конфе') 
            elif p == pr_st and start == 0:
                n -= sp + 1 - p
                print(f'Компьютер взял {sp + 1 - p}. Осталось {n} конфе') 
            else:
                pr_co = sp - p + 1
                n -= pr_co
                if n <= 0:
                    print(f'Компьютер взял {pr_co} и ___ПОБЕДИЛ!___')
                    break
                print(f'Компьютер взял {pr_co}. Осталось {n} конфе')       
        co += 1    

    
    while n > 0:
        if co%2 != 0: #  первый ход компьютера
            p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
            if 1 > p or p > sp:
                while re < 3:
                    print(f'Неверное число. Введите число от 1 до {sp}: ')     
                    p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
                    if 0 < p < sp + 1:
                        break
            n -= p
            if n <= 0:
                print('Победа первого игрока')
                break
            print(f'Осталось {n} конфет')
        else:
            if n > f_start//2:
                temp = random.randint(1, sp+1)
                n -= temp
                print(f'Компьютер взял {temp}. Осталось {n} конфе')  
            elif p < pr_st and start == 0:
                start += 1
                n -= pr_st - p
                print(f'Компьютер взял {pr_st - p}. Осталось {n} конфе') 
            elif p > pr_st and start == 0:
                start += 1
                n -= pr_st + sp + 1 - p
                print(f'Компьютер взял {pr_st + sp + 1 - p}. Осталось {n} конфе') 
            elif p == pr_st and start == 0:
                n -= sp + 1 - p
                print(f'Компьютер взял {sp + 1 - p}. Осталось {n} конфе') 
            else:
                pr_co = sp - p + 1
                n -= pr_co
                if n <= 0:
                    print(f'Компьютер взял {pr_co} и ___ПОБЕДИЛ!___')
                    break
                print(f'Компьютер взял {pr_co}. Осталось {n} конфе')       
        co += 1   






# def PvComp_int(n, sp): 
    
#     pr_st = n % (sp + 1)
#     re = 0
#     co = 1
#     start = 0

#     while n > 0:
#         if co%2 != 0: 
#             p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
#             if 1 > p or p > sp:
#                 while re < 3:
#                     print(f'Неверное число. Введите число от 1 до {sp}: ')     
#                     p = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {sp}: '))
#                     if 0 < p < sp + 1:
#                         break
#             n -= p
#             if n <= 0:
#                 print('Победа первого игрока')
#                 break
#             print(f'Осталось {n} конфет')
#         else:
#             if p < pr_st and start == 0:
#                 start += 1
#                 n -= pr_st - p
#                 print(f'Компьютер взял {pr_st - p}. Осталось {n} конфе') 
#             elif p > pr_st and start == 0:
#                 start += 1
#                 n -= pr_st + sp + 1 - p
#                 print(f'Компьютер взял {pr_st + sp + 1 - p}. Осталось {n} конфе') 
#             elif p == pr_st and start == 0:
#                 n -= sp + 1 - p
#                 print(f'Компьютер взял {sp + 1 - p}. Осталось {n} конфе') 
#             else:
#                 pr_co = sp - p + 1
#                 n -= pr_co
#                 if n <= 0:
#                     print(f'Компьютер взял {pr_co} и ___ПОБЕДИЛ!___')
#                     break
#                 print(f'Компьютер взял {pr_co}. Осталось {n} конфе')      
#         print(' ') 
#         co += 1   



def main():
    num = int(input('Введите число: '))
    step = int(input('Введите шаг хода: '))
    game_whiht = int(input('Введите с кем будите играть \nЧеловек против Человека - введите [1]: \nПротив Компьютера - введите [2]: \n'))
    if game_whiht == 1:
        pvp(num, step)
    else:
        PvComp(num, step)
 

if __name__ == "__main__":
	main()