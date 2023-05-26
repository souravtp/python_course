"""child classes are inherited from parent class and go on"""

class Vehicle:  # This is a parent class.
    def vehicle_info(self):
        return"Inside Vehicle Class"


class Car(Vehicle):  # This is a child class with inherited properties of parent class.
    def car_info(self):
        return"Inside Car Class"


class SportsCar(Car):  # this is child class with inherited properties of parent and its parent class.
    def sports_car_info(self):
        return"Inside Sports Car Class"


v = SportsCar()
print(v.sports_car_info())
print(v.car_info())
