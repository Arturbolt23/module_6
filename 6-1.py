class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False
    def __str__(self):
        return self.name
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}не стал есть {food.name} и умер с голода')
            self.alive = False


class Plant:
    def __init__(self,name):
        self.name = name
        self.edible = False
    def __str__(self):
        return self.name


class Mammal(Animal):
    pass
    # def eat(self, food):
    #     if food.edible:
    #         print(f'{self.name} съел {food.name}')
    #         self.fed = True
    #     else:
    #         print(f'{self.name}не стал есть {food.name} и умер с голода')
    #         self.alive = False
'''
вынес из классов дочерних все в родит.клас, все рабоатет
'''

class Predator(Animal):
    pass
    # def eat(self, food):
    #     if food.edible:
    #         print(f'{self.name} съел {food.name}')
    #         self.fed = True
    #     else:
    #         print(f'{self.name}не стал есть {food.name} и умер с голода')
    #         self.alive = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
