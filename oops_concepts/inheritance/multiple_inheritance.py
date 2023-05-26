"""child classes are inherited from multiple parent classes"""


class Vehicle:  # this is a parent class
    def vehicle_info(self):
        return "Inside Vehicle Class"


class Car:  # This is another parent class
    def car_info(self):
        return "Inside Car Class"


class SportsCar(Car, Vehicle):  # This is a child class with inherited properties of both parent classes.
    def sports_car_info(self):
        return "Inside Sports Car Class"


obj = SportsCar()
print(obj.vehicle_info())
print(obj.car_info())

obj2 = Vehicle()
# print(obj2.sports_car_info)  # here the parent class does not use the methods inside child classes
# obj2.car_info()  # same in here also.
