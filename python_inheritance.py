class Car:
    def __init__(self, name):
        self.name = name
    
    def model(self):
        return "..."

class BMW(Car):
    def model(self):
        return "M340i"

b = BMW("BMW")
print(b.name)
print(b.model())



class Vehicle:
    def __init__(self, make):
        self.make = make

class Car(Vehicle):
    def __init__(self, make, doors):
        super().__init__(make)
        self.doors = doors

c = Car("BMW", 4)
print(c.make)
print(c.doors)


#simple inheritance 
class Parent:
    def name_is(self):
        print("this is a parent class")

class Child(Parent):
    def name_is(self):
        super().name_is()
        print("this is a child class")

c = Child()
c.name_is()