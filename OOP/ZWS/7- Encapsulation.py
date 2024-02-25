
# class Member:

#     def __init__(self, name):

#         self.name = name    # Public


# one = Member("John")
# print(one.name)

# one.name = "Jane"
# print(one.name)

############################################################################
# Protected Attributes and methods Can be accessed from within the class or sub-classes
# Attributes or methods are prefixed with one underscore _


# class Member:

#     def __init__(self, name):

#         self._name = name    # Protected


# one = Member("John")
# print(one._name)

# one._name = "Jane"
# print(one._name)



############################################################################
# Private Attributes and methods Can be accessed from within the class or Object only
# Attributes can't be modified from outside the class
# Attributes or methods are prefixed with two underscore __



class Member:

    def __init__(self, name):

        self.__name = name    # Private

    def say_hello(self):
        print(f"Hello {self.__name}")


one = Member("John")
#print(one.__name)       # AttributeError: 'Member' object has no attribute '__name'

one.say_hello()

print(one._Member__name)