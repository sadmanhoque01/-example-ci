def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit<-459.67:
        raise  AssertionError("Temp below abs zero")
    return multiply(subtract(fahrenheit, 32), 5 / 9)