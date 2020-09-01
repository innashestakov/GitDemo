class Example:           # declare class

    c = 100

    def __init__(self, a, b):   # The parameterized constructor take its first argument as a reference
                                # to the instance being constructed known as self
                                # and the rest of the arguments are provided by the programmer.
        self.a = a
        self.b = b

    def sum(self):
        print(self.a + self.b)

    def greet(self):
        print("Hello")

    def additional_sum(self):
        print(Example.c + self.a + self.b)    # "Example.c" this is class variable and could not be changed in the objects


obj = Example(5, 6)
obj.greet()
obj.sum()
print(obj.c)
obj.additional_sum()
