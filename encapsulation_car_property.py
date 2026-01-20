class Car:
    def __init__(self):
        self.__engine_started = False

    @property
    def engine_started(self):
        return self.__engine_started

    @engine_started.setter
    def engine_started(self , val):
        
        if isinstance(val, bool):
            self.__engine_started = val
            if val:
                print("engine started")
            else:
                print("engine stopped")

        else:
            print("Engine state is on halt")

car1 = Car()
print("Running" if car1.engine_started else "OFF")