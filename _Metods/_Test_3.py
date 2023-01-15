def PvComp(n, sp):  # Компьютер ходит первым
    re = 0
    co = 1
    start = 0
    while n > 0:
        if co%2 == 0: #  первый ход компьютера
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
            if start == 0:
                start += 1
                pr_st = n % (sp + 1)
                n -= pr_st
                print(f'Компьютер взял {pr_st}. Осталось {n} конфе') 
            else:
                pr_co = sp - p + 1
                n -= pr_co
                if n <= 0:
                    print(f'Компьютер взял {pr_co} и ___ПОБЕДИЛ!___')
                    break
                print(f'Компьютер взял {pr_co}. Осталось {n} конфе')            
        co += 1    
