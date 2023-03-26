from Cat import Cat
from Dog import Dog
from Animal import Animal

class Vet_service:
    def __init__(self):
        list1 = []
        self._list1 = list1

    def add_animal(self, animal):
        self._list1.append(animal)

    def del_animal(self, animal):
        self._list1.remove(animal)

    def print(self):
        for el in self._list1:
            print(str(el))
       
    def getAni(self, i):
        return self._list1[i]
    
 