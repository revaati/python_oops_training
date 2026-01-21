from multipledispatch import dispatch

@dispatch(int)
def func(x):
    return x*x

@dispatch(str)
def func(x):
    return x

@dispatch(float)
def func(x):
    return x*2

print(func(5))
print(func("Revati"))
print(func(0.3))