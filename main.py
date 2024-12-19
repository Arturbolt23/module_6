
class Human:
    head = True
    _legs = True
    __arms = True
    # def __init__(self, name):
    #     self.name = name

    def say_hello(self):
        print(f"hello i'm,{self.name}")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    # def about(self):
    #     print("I'm a student")
    arms = False
    pass


class Teacher(Human):
    pass

human = Human()
human.about()
student = Student()
student.about()

print(dir(human))
print(dir(student))
print(student.Human.__arms)