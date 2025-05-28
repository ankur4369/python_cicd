from abc import ABCMeta, abstractmethod

class MyAbstractInterface(metaclass=ABCMeta):

    @abstractmethod
    def my_func():
        pass

class MyInterface():
    def my_func(self):
        pass
    
    def my_way(self):
        print("My Interface Way")


class MyDog(MyInterface):

    def my_func(self):
        print("I am a dog")


class MyCat(MyInterface):

    def my_func(self):
        print("I am a cat")


class Application:

    def __init__(self, animal):
        self.animal = animal
    
    def get_animal(self):
        self.animal.my_func()
        self.animal.my_way()


dog = MyDog()
cat = MyCat()
a = Application(dog)
b = Application(cat)
a.get_animal()
b.get_animal()
