# class University:  # This is called the base class or superclass
#     def __init__(self):
#         self.name1 = "Yale University"
#         print("You are in University Class Constructor")
#
#     def test(self):
#         print("test function")
#
#
# class College(University):
#     def __init__(self):
#         super().__init__()
#         self.name2 = "Yale School of Medicine"
#         print("You are in College Class Constructor")
#
#     def show(self):
#         print(self.name2)
#
#
# obj1 = University()
# # University()
# print(obj1.name1)
# # obj1.test()
#
#
# obj2 = College()
# print(obj2.name2)
# obj2.test()
# print(obj2.name1)  # this attribute can be accessed only if we add super().__init__() in child class.

"""using attributes in parent classes and child class"""


# class University:
#     def __init__(self, name1):
#         self.name1 = name1
#         print("You are in University Class Constructor", self.name1)
#
#     def test(self):
#         print("test function")
#
#
# class College(University):
#     def __init__(self, name2):
#         super().__init__(name2)
#         self.name2 = name2
#         print("You are in College Class Constructor")
#
#     def show(self):
#         print(self.name2)
#
#
# obj1 = University("harvard")
# print(obj1.name1)
#
# obj2 = College('oxford')
# print(obj2.name1)  # here the child class argument 'oxford' is getting printed.
# print(obj2.name2)

"""usage of super().__init__()"""


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print("Vehicle details: ", self.make, self.model, self.year)


class Car(Vehicle):
    def __init__(self, make, model, year, color):  # here we can give any extra attributes.
        super().__init__(make, model, year)  # here we have to give all the arguments in the parent class.
        self.color = color
        print("Car details: ", self.make, self.model, self.year, self.color)

    def get_model(self):
        print(f'model:{self.model}')


car1 = Car("Toyota", "Corolla", 2021, "Red")
car1.get_model()
