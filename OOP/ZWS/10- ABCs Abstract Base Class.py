
# Abstract Class => Pattern --> Any Class MUST follow this pattern 

# Abstract Base Class =>    

# ABCMeta class is a meta class used for defining Abstract Base Class

from abc import ABCMeta, abstractmethod


class Programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):
        pass
   

class Python(Programming):

    def has_oop(self):
        return "Yes"
    

    
class Pascal(Programming):

    def has_oop(self):
        return "No"
    
class C(Programming):

    pass

#one = Programming()
#one.has_oop()       # TypeError: Can't instantiate abstract class Programming with abstract method has_oop


python = Python()
print(python.has_oop())

pascal = Pascal()
print(pascal.has_oop())

c = C()
print(c.has_oop())    

    
