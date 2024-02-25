

class Member:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello {self.name}"

    def age_in_days(self):
        return self.age * 365
    
    # Function that don't do any action .. Just it returns a value => Consider it a property / Attribute by adding a property decorator [ @property ]

    @property
    def age_in_years_property(self):
        return self.age * 365
    

one = Member("Ahmed", 40)
print(one.name, ' ' ,one.age)

print(one.say_hello())
print(one.age_in_days())

print("*" * 20)

print(one.age_in_years_property)