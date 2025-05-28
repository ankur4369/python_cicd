from abc import ABCMeta, abstractmethod

class Builder(metaclass=ABCMeta):

    @abstractmethod
    def build(self):
        pass

class SandwichBuilder(Builder):

    def choose_bread(self, bread):
        self._bread = bread
    
    def add_cheese(self):
        self._cheese = True
    
    def add_toppings(self, *args):
        self._toppings = args
    
    def add_sauce(self, *args):
        self._sauce = args
    
    def build(self):
        self.choose_bread("Honey and Oats")
        self.add_toppings('Jalapeno', 'Bell Peppers', 'Pickles')
        self.add_sauce('Mayo', 'Honey')
        return f"I am a SANDWICH with ingredients as - \n {getattr(self, '_bread', 'No')} bread, {getattr(self, '_cheese', 'No')} cheese, {getattr(self, '_toppings', 'No')} toppings and {getattr(self, '_sauce', 'No')} sauce"

class SaladBuilder(Builder):
    
    def add_cheese(self):
        self._cheese = "Mozarella"
    
    def add_toppings(self, *args):
        self._toppings = args
    
    def add_sauce(self, *args):
        self._sauce = args

    def build(self):
        self.add_cheese()
        self.add_toppings('Tomato', 'Onions')
        self.add_sauce('Sweet Chilli')
        return f"I am a SANDWICH with ingredients as - \n {getattr(self, '_bread', 'No')} bread, {getattr(self, '_cheese', 'No')} cheese, {getattr(self, '_toppings', 'No')} toppings and {getattr(self, '_sauce', 'No')} sauce"


c = SandwichBuilder()
d = SaladBuilder()
print(c.build())
print(d.build())