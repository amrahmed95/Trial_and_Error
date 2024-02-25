# Polymorphism => Multi-forms (same function name , different action)

# Method Overriding
# Method Overloading

class A:

    def do_something(self):

        print("Doing something")

        # This error will show if the function do_something() is not implemented in the derived classes
        raise NotImplementedError("Derived class must implement this method")   


class B(A):

    def do_something(self):

        print("Doing something else (From Class B)")

    pass


class C(A):
    pass

my_instance_B = B()
my_instance_B.do_something()

my_instance_C = C()
my_instance_C.do_something()
