class MyFirstClass:
    a = 2
    b = 5

    def __get__(self):
        return self.a

    def __set__(self, b):
        self.b = b
        return self.b
    
    def __call__(self):
        return ("Thanks for calling me!")


b = type("MySecondClass", (), {'a': 10, 'b': 20, 'c': 30})
# print(type(b), b.a, b.b, b.c)

class Dog:
    def show(self):
        print("I am a dog!")

class BullDog(Dog):

    def show(self):
        print("I am a bull dog")

    def bark(self):
        print("I am a bull dog and I can bark")

def show(Object):
    print("I am a LAB dog")

lab_dog = type("LabDog",  (Dog,), {'show': show})

new_dog = BullDog()
new_dog_1 = lab_dog()
new_dog.show()
new_dog_1.show()