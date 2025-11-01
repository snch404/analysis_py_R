#Print Fibonacci series up to n numbers without recursion
def fib(n):
    for i in range(n):
        if i == 0:
            a = 0
            print(a, end=' ')
        elif i == 1:
            b = 1
            print(b, end=' ')
        else:
            c = a + b
            print(c, end=' ')
            a = b
            b = c
n = int(input("Enter the number of terms in the Fibonacci series: "))
print("Fibonacci series up to", n, "terms:")
fib(n)