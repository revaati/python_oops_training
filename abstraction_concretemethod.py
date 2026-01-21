from abc import ABC , abstractmethod

class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def horn(self):
        return "Honk Honk!!"

class Kia(Car):
    def start_engine(self):
        return "Kia engine started"

    def stop_engine(self):
        return "Kia engine stopped"

class BMW(Car):
    def start_engine(self):
        return "BMW engine started"

    def stop_engine(self):
        return "BMW engine stopped"

kia = Kia()
BMW = BMW()

print(kia.start_engine())
print(kia.stop_engine())
print(kia.horn())