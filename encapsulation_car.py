class Car:
    def __init__(self):
        self.__engine_started = False

    def start_engine(self):
        self.__engine_started = True
        print("Engine started..")

    def stop_engine(self):
        self.__engine_started = False
        print("Engine stopped ..")

    def status(self):
        return "running" if self.__engine_started else "OFF"

car1 = Car()
print(car1.status())
car1.start_engine()
print(car1.status())
car1.stop_engine()
print(car1.status())