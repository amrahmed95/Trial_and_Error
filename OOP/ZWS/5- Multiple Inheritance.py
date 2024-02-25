class BaseOne:

    def __init__(self) -> None:
        print("BaseOne")
    
    def func_one(self):
        print("Func One")


class BaseTwo:

    def __init__(self) -> None:
        print("BaseTwo")

    def func_two(self):
        print("Func Two")
    

class Derived(BaseOne, BaseTwo):
    pass


my_var = Derived()

#print(Derived.mro())

print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()



##############################################################

class Base:

    pass

class DerivedOne(Base):

    pass

class DerivedTwo(DerivedOne):

    pass



