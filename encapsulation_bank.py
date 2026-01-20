class Bank:
    def __init__(self , balance):
        self.__balance = balance

    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited :", amount)
        else:
            print("Invalid amount")

    def withdraw(self , amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance-=amount
            print("withdrawn : ", amount)
        else:
            print("Insufficient balance")
            
    def get_balance(self):
        return self.__balance

acc = Bank(10000)
print(acc.get_balance())
acc.withdraw(1000)
acc.deposit(5000)


#using @property

class Bank1:
    def __init__(self , balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self , amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")

acc1 = Bank1(10000)
print(acc1.balance)
acc1.balance = 1500
print(acc1.balance)
acc1.balance = 500
