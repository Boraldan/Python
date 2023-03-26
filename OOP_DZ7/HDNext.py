from HotDrink import HotDrink

class HDNext(HotDrink):
    def __init__(self, name, volume, temp):
        super().__init__(name, volume)
        self._temp = temp
 

    @property
    def temp(self):
        return self._temp
 
    @temp.setter
    def temp(self, new_temp):
        self._temp = new_temp

    def __str__(self)  -> str:
        return f"{self._name} --- {self._volume} ml --- {self._temp} t "

