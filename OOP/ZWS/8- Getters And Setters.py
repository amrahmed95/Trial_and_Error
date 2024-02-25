
class Member:
    def __init__(self, name) :
        self.__name = name

    def say_hello(self):
       return f"Hello {self.__name}"
    
    def get_name(self):          # Getter
        return self.__name
    
    def set_name(self, new_name): # Setter
        self.__name = new_name

m = Member("John")

#print(m.__name) # Error
#print(m._Member__name) # No Error (NO Restriction in Python)

#print(m.say_hello())

print(m.get_name())

m.set_name("Jane")

print('New name is: ',m.get_name())