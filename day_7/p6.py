def add(a, b):
    return a + b

# Decorator definition
def positive_only(func):
    def inner(a, b):
        if a < 0:
            a = 0
        if b < 0:
            b = 0
        return func(a, b)
    return inner


# Taking user input
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))

# Without decorator
print("Without using decorator sum is", add(a, b))

# Applying decorator manually
add = positive_only(add)

# With decorator
print("With using decorator function sum is", add(a, b))
