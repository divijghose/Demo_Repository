def add(x,y):
    return x + y

def subtract(x,y):
    return abs(x-y)

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x/y

print(add(3,4))

print(subtract(3,4))
