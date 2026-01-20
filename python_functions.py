def add(a,b):
    return a+b

x = int(input())
y = int(input())

result = add(x,y)
print(result)


def car(name):
    if name == '':
        print("You didn't enter the car name!")
    else:
        print("Its a")
        for letter in name:
            print(letter)

name = input("Car name: ")
car(name)