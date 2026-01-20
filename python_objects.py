#basic python class
class Person:
    pass
p = Person()

#new objectand method
class Person:
    def __init__(self , name = ""):
        self.val = name
        
    def new_name(self):
        return self.val
    
p2 = Person("revati")
p2.new_name()
print(p2.val)
