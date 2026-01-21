class Vehicle:
    def show_type(self):
        print("Vehicle used for transportation")

class Car(Vehicle):
    def car_features(self):
        print("Car has 4 wheels and AC")

class Electric:
    def battery_info(self):
        print("Electric : runs on battery")


class ElectricCar(Car , Electric):
    def feature(self):
        print("ElectricCar : ecofriendly and silent")

ecar = ElectricCar()
ecar.show_type()
ecar.car_features()
ecar.battery_info()
ecar.feature()