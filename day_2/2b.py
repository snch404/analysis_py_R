#factorial of number using recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
a = int(input("Enter a number to find its factorial: "))
if a < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("The factorial of", a, "is", factorial(a))