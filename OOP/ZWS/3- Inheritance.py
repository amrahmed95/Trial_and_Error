class Food: # Base Class
    def __init__(self,name, price):
        self.name = name
        self.price = price
        print(f"{self.name} is created from base class and price is {self.price}")
    
    def eat (self):
        print("Eating Method from base class")


class Apple(Food): # Derived Class
    def __init__(self, name, price, amount):

        #self.name = name                   
        #self.price = price

        #Food.__init__(self,name,price)       # Create Instance from base Class

        super().__init__(name,price+20)         # Create Instance from base Class
        
        self.amount = amount                  # Create Instance (not in base class)

        print(f"{self.name} is created from Derived class and price is {self.price} and amount is {self.amount}")

    def get_from_tree(self):
        print("Apple is from tree")
    


food_one = Food("Pizza", 150)
food_one.eat()


print("*"*50)


food_two = Apple("Apple", 150, 10)
food_two.eat()
food_two.get_from_tree()
