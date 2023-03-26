from Cat import *
from Dog import *
from Vet_service import *

cat1 = Cat('Барсик', 5, 25, False)
dog1 = Dog('Шарик', 7, 20, True)

 

list_animal = Vet_service()
list_animal.add_animal(cat1)
list_animal.add_animal(dog1)
# list_animal.print()
# list_animal.del_animal(cat1)
# print('______________________')
# list_animal.print()

# print(cat1.nickname)
 
# li = []
# li.append(cat1)
# li.append(dog1)
 

li_cat = []

li_cat.append(list_animal.getAni(0))

print(li_cat[0])