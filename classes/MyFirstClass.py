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


a = MyFirstClass()
print(MyFirstClass()())
print(a, a())