#factorial of a number using iteration
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
a=int(input("Enter a number to find its factorial: "))
print("Factorial of", a, "is", factorial(a))