class student:
    def __init__(self, name ,mark):
        self.name = name
        self.mark = mark

s = student("Revati", 50)
print(s.name)
print(s.mark)


# Protected members (_var)

class student:
    def __init__(self , name , mark):
        self._mark = mark

class result(student):
    def show(self):
        print(self._mark)

r = result("Revati" , 50)
r.show()


# Private members (__var)

class student:
    def __init__(self , name , mark):
        self.__mark = mark

    def show(self):
        print(self.__mark)

s = student("revati" , 70)
s.show()
# print(s.__mark)


#