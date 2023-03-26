
from HotDrink import HotDrink
from HDNext import HDNext

class HDAutomat:
    def __init__(self):
        li = []
        self._li = li

    def add_drink(self, HotDrink):
        self._li.append(HotDrink)

    def del_drink(self, HotDrink):
        self._li.remove(HotDrink)

    def print(self):
        for el in self._li:
            print(str(el))
       
    def get_drink(self, i):
        return self._li[i]
    
    def get_temp(self, t):
        flag = True
        for el in self._li:
          if el.temp <= t:
            print(el)
            flag = False
        if flag:
            print("Нет напитка с такой температурой")
 
