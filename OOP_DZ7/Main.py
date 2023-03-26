from HotDrink import *
from HDNext import *
from HDAutomat import *

tea = HDNext("tea100", 200, 100)
tea2 = HDNext("tea70", 150, 70)
tea3 = HDNext("tea50", 100, 50)
cofe = HDNext("cofe100", 100, 100)
cofe2 = HDNext("cofe70", 100, 70)
cofe3 = HDNext("cofe50", 100, 50)

list_HD = HDAutomat()
list_HD.add_drink(tea)
list_HD.add_drink(tea2)
list_HD.add_drink(tea3)
list_HD.add_drink(cofe)
list_HD.add_drink(cofe2)
list_HD.add_drink(cofe3)

list_HD.print()

print("-------------------")
 
list_HD.get_temp(55) # поиск напитка до определенной температуры