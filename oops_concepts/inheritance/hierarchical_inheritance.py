"""multiple child classes with inherited properties from a single parent class"""


class Vehicle:  # This is a parent class
    def info(self):
        print("This is vehicle")


class Car(Vehicle):  # This is a child class
    def car_info(self, name):
        print("car name2 is", name)


class Truck(Vehicle):  # This is another child class
    def truck_info(self, name):
        print("truck name2 is", name)


obj1 = Car()
obj1.car_info('BMW')
obj1.info()

obj2 = Truck()
obj2.truck_info("Ford")
obj2.info()
