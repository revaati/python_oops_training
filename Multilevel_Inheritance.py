class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(self.make + " " + self.model + "'s engine is now running.")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def honk_horn(self):
        print(self.make + " " + self.model + "'s horn goes 'Honk! Honk!'")

class SportsCar(Car):
    def __init__(self, make, model, doors, top_speed):
        super().__init__(make, model, doors)
        self.top_speed = top_speed

    def show_info(self):
        print("This is a " + self.make + " " + self.model + " sports car with " + str(self.doors) + " doors.")
        print("It can reach a top speed of " + str(self.top_speed) + " mile per hour.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, has_kickstand):
        super().__init__(make, model)
        self.has_kickstand = has_kickstand

    def display_kickstand_status(self):
        if self.has_kickstand:
            print(self.make + " " + self.model + " has a kickstand.")
        else:
            print(self.make + " " + self.model + " does not have a kickstand.")

car = Car("Toyota", "Camry", 4)
sports_car = SportsCar("Ferrari", "488 GTB", 2, 205)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", True)

car.start_engine()
car.honk_horn()

sports_car.start_engine()
sports_car.honk_horn()
sports_car.show_info()

motorcycle.start_engine()
motorcycle.display_kickstand_status()
