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

#multilevel inheritance
class GrandParent:
    def name_is(self):
        print("this is a grandparent class")

class Parent(GrandParent):
    def name_is(self):
        super().name_is()
        print("this is a parent class")

class Child(Parent):
    def name_is(self):
        super().name_is()
        print("this is a child class")

c = Child()
c.name_is()


# multiple inheritance

class Father:
    def name_is(self):
        print("this is a father class")

class Mother:
    def name_is(self):
        print("this is a mother class")

class Child(Father , Mother):
    def name_is(self):
        Father.name_is(self)
        Mother.name_is(self)
        print("this is a child class")

c = Child()
c.name_is()

# Hybrid Inheritance

class Person:
    def intro(self):
        print("I am a Person")

class Father(Person):
    def intro(self):
        print("I am a Father")
        super().intro()

class Mother(Person):
    def intro(self):
        print("I am a Mother")
        super().intro()

class Child(Father, Mother):
    def intro(self):
        print("I am a Child")
        super().intro()

c = Child()
c.intro()

