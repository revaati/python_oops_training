
from functools import singledispatch

@singledispatch
def service_request(item):
    raise TypeError("Unsupported type ")

@service_request.register
def _(item: str):
    return f"Service request by registration number: {item}"

class Car:
    def __init__(self, model): 
        self.model = model

@service_request.register
def _(item: Car):
    return f"Service request for car model: {item.model}"

print(service_request("MH12AB1234"))
print(service_request(Car("Sedan")))
