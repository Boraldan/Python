import os  #  очистка consol
os.system('cls||clear')
# ---------------------------


desk = [[0,1,1], 
        [0,0,0], 
        [0,1,0]]


def check_desk(desk: list, symbol: str) -> bool:
    for i in range(3):
        if desk[i].count(symbol) == 3:
            return True
        elif [desk[0][i], desk[1][i], desk[2][i]].count(symbol) == 3:
            return True
        elif [desk[0][0], desk[1][1], desk[2][2]].count(symbol) == 3:
            return True
        elif [desk[0][2], desk[1][1], desk[2][0]].count(symbol) == 3:
            return True
    return False

    # for i in range(3):
    # if desk[i].count(symbol) == 3:

# num = desk[i].count(1)



print(check_desk(desk))