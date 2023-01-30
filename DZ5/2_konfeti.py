# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
#  последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все
#   конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
os.system('cls||clear')

def pvp(num, step):
    re = 0
    count = 1
    while num > 0:
        if count%2 != 0:
            plr_step = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {step}: '))
            if 1 > plr_step or plr_step > step:
                while re < 3:
                    print(f'Неверное число. Введите число от 1 до {step}: ')     
                    plr_step = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {step}: '))
                    if 0 < plr_step < step + 1:
                        break
            num -= plr_step
            if num <= 0:
                print('Победа первого игрока')
                break
            print(f'Осталось {num} конфет')
        else:
            plr_step = int(input(f'Ход ВТОРОГО игрока. Введите число от 1 до {step}: '))
            if 1 > plr_step or plr_step > step:
                while re < 3:
                    print(f'Неверное число. Введите число от 1 до {step}: ')     
                    plr_step = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {step}: '))
                    if 0 < plr_step < step + 1:
                        break
            num -= plr_step
            if num <= 0:
                print('Победа второго игрока')
                break
            print(f'Осталось {num} конфет')
        count += 1

    print('------------Игра закончена----------------')

def PvComp_1(num, step):  # Компьютер ходит первым
    re = 0
    count = 1
    start_step = 0
    while num > 0:
        if count%2 == 0: 
            plr_step = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {step}: '))
            if 1 > plr_step or plr_step > step:
                while re < 3:
                    print(f'Неверное число. Введите число от 1 до {step}: ')     
                    plr_step = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {step}: '))
                    if 0 < plr_step < step + 1:
                        break
            num -= plr_step
            if num <= 0:
                print('Победа первого игрока')
                break
            print(f'Осталось {num} конфет')
        else:
            if start_step == 0:
                start_step += 1
                pr_st = num % (step + 1)
                num -= pr_st
                print(f'Компьютер взял {pr_st}. Осталось {num} конфет') 
            else:
                pr_co = step - plr_step + 1
                num -= pr_co
                if num <= 0:
                    print(f'Компьютер взял {pr_co} и ___ПОБЕДИЛ!___')
                    break
                print(f'Компьютер взял {pr_co}. Осталось {num} конфет')            
        count += 1    

def PvComp_2(num, step):   # компьютер ходит вторым
    
    plr_fist = num % (step + 1)
    re = 0
    count = 1
    flag_start = 0

    while num > 0:
        if count%2 != 0: 
            plr_step = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {step}: '))
            if 1 > plr_step or plr_step > step:
                while re < 3:
                    print(f'Неверное число. Введите число от 1 до {step}: ')     
                    plr_step = int(input(f'Ход ПЕРВОГО игрока. Введите число от 1 до {step}: '))
                    if 0 < plr_step < step + 1:
                        break
            num -= plr_step
            if num <= 0:
                print('Победа первого игрока')
                break
            print(f'Осталось {num} конфет')
        else:
            if plr_step < plr_fist and flag_start == 0:
                flag_start += 1
                num -= plr_fist - plr_step
                print(f'Компьютер взял {plr_fist - plr_step}. Осталось {num} конфет') 
            elif plr_step > plr_fist and flag_start == 0:
                flag_start += 1
                num -= plr_fist + step + 1 - plr_step
                print(f'Компьютер взял {plr_fist + step + 1 - plr_step}. Осталось {num} конфет') 
            elif plr_step == plr_fist and flag_start == 0:
                num -= step + 1 - plr_step
                print(f'Компьютер взял {step + 1 - plr_step}. Осталось {num} конфет') 
            else:
                plr_comp = step - plr_step + 1
                num -= plr_comp
                if num <= 0:
                    print(f'Компьютер взял {plr_comp} и ___ПОБЕДИЛ!___')
                    break
                print(f'Компьютер взял {plr_comp}. Осталось {num} конфет')      
        print(' ') 
        count += 1    

def main():
    num = int(input('Введите число: '))
    step = int(input('Введите шаг хода: '))
    game_whiht = int(input('Введите с кем будите играть \nЧеловек против Человека - введите [1]: \nПротив Компьютера - введите [2]: \n'))
    if game_whiht == 1:
        pvp(num, step)
    else:
        game_whiht = int(input('Кто будет ходить первым? \nКомпьютер - введите [1]: \nЧеловек - введите [2]: \n'))
        if game_whiht == 1:
            PvComp_1(num, step)
        else:
            PvComp_2(num, step)
 

if __name__ == "__main__":
	main()