import os  #  очистка consol
os.system('cls||clear')
# ---------------------------

li = [1, 5, 2, 3, 4, 6, 1, 7]
print(li)
li = list(map(lambda x: x**2 , li ) )
print(li)