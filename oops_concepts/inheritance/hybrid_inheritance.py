class Vehicle:
    def info(self):
        print("this is a vehicle")


class Car(Vehicle):
    def car_info(self, name):
        print("car name2 is", name)


class Truck(Vehicle):
    def truck_info(self, name):
        print("truck name2 is", name)


class Sports_Car(Car, Vehicle):
    def sports_car_info(self, name):
        print("inside sports car class")