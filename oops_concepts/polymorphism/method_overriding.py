"""
Method overloading allows a single class to have multiple methods with the same name2,
but with different parameters. This allows objects of the same class to be used in different contexts,
depending on the parameters passed to the method.
"""


class A:
    def func1(self):
        print("function one working")

    def func(self):
        print("function working from class A")


class B(A):
    def func3(self):
        print("function three working")

    def func(self):
        print("function working from class B")
        # super().func()


obj = B()

obj.func1()
obj.func3()
obj.func()  # since we defined same function in child class, the parent method is overridden by it.
# If we want to call parent function, we can use super().func() in child class.

# obj2 = A()
# obj2.func()

"""Here we cannot access the show method from parent class from child class, since it is overriden.
If we need to access the parent class method from child class, we have to use super().method() in child class
def show(self):
    super().show()
    print(self.value())
"""

"""another example"""


# class Vehicle:
#     def __init__(self, name2, color, price):
#         self.name2 = name2
#         self.color = color
#         self.price = price
#
#     def show(self):
#         print('Details', self.name2, self.color, self.price)
#
#     def max_speed(self):
#         print('max speed is 150')
#
#     def change_gear(self):
#         print('vehicle change 6 gear')
#
# class Car(Vehicle):
#     def max_speed(self):
#         print('car max speed is 240')
#
#     def change_gear(self):
#         print('gear change 7 gears')
#
#
# car = Car('force', 'grey', 25000)
# # car.show()
#
# vehicle = Vehicle('lorry', 'black', 100000)
# # vehicle.show()
#
#
# for i in (car, vehicle):
#     i.max_speed()
#     i.change_gear()
#     i.show()
