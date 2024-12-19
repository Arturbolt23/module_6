from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, x, y, z, speed):
        self._cords = [x, y, z]
        self.speed = speed

    # def __str__(self):
    #     return f"Animal(живой?- {self.live}, звуки-{self.sound}, положение-{self._cords}"

    def move(self,dx,dy,dz):
        dx *= self.speed
        dy *= self.speed
        dz *= self.speed
        if self._cords[2] + dz < 0:
            print("It's too deep, i can't dive:(")
        else:
            self._cords[0] += dx
            self._cords[1] += dy
            self._cords[2] += dz

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER >=5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        count = randint(1,4)
        print(f'Here are {count} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        speed_in_dive = self.speed / 2
        self._cords[2] -= dz * speed_in_dive


class PoisonusAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonusAnimal, AquaticAnimal):
    sound = 'Click-click-click'
    def __init__(self, speed):
        super().__init__(0, 0, 0, speed)
        self.name = 'Утконос'

    def __str__(self):
        return f"{self.name} живой? - {self.live}, звуки - {self.sound}, положение - {self._cords})"



db = Duckbill(10)

print(db.live)

print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()

print(db)
'''
думал как добавить логику, чтобы при создании нового животного передавать ему русское имя,
и выводить в последнем принте информацию об этом животном, в отдельном случае с утконосом сделал - заработало, когда 
стал переносить в класс Animal поплыл. подскажите пожалуйста, какой алгоритм действий для реализации этого момента?
'''