from abc import ABCMeta, abstractmethod

class SandwichBuilder(metaclass=ABCMeta):

    @abstractmethod
    def choose_bread(self):
        print("DEFAULT BASE")
    
    @abstractmethod
    def add_toppings(self):
        print("DEFAULT TOPPINGS")

    @abstractmethod
    def add_sauce(self):
        print("DEFAULT SAUCE")
    
    def build_sandwich(self):
        self.choose_bread()
        self.add_toppings()
        self.add_sauce()
    
    def get_sandwich(self):
        self.build_sandwich()
        return f"Sandwich - {self.bread} \n Toppings - {self.toppings} \n Sauce - {self.sauce}"

class VeggiePattySandwichBuilder(SandwichBuilder):

    def choose_bread(self):
        self.bread = "Honey and Oats"
    
    def add_toppings(self):
        self.toppings = []
        self.toppings.extend(["Jalapeno", "Bell Peppers", "Pickles"])

    def add_sauce(self):
        self.sauce = []
        self.sauce.extend(["Margarita Spicy", "Sweet Chilli"])

class VeggieSandwichBuilder(SandwichBuilder):

    def choose_bread(self):
        self.bread = "Italian & Herbs"
    
    def add_toppings(self):
        self.toppings = []
        self.toppings.extend(["Tomato", "Onions", "Olives"])

    def add_sauce(self):
        self.sauce = []
        self.sauce.extend(["Mayo", "Honey"])

c = VeggiePattySandwichBuilder()
d = VeggieSandwichBuilder()
print(c.get_sandwich())
print(d.get_sandwich())