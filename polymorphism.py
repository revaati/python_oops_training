
class Car:
    def start(self):
        return "Car: ignition on"

    def drive(self):
        return "Car: driving"

class Sedan(Car):
    def start(self):
        return "Sedan: push-button start"

    def drive(self):
        return "Sedan: smooth city drive"

class SUV(Car):
    def drive(self):
        return "SUV: off-road capable drive"

class ElectricCar(Car):
    def start(self):
        return "EV: systems online "

    def drive(self):
        return "EV: instant torque drive"

vehicles = [Car(), Sedan(), SUV(), ElectricCar()]
for vehicle in vehicles:
    print(vehicle.start(), "|", vehicle.drive())
