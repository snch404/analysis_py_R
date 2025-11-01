ch=input("Enter + for Addition, - for Subtraction, * for Multiplication, / for Division:")
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
if ch=='+':
    print("Addition is:", a+b)
elif ch=='-':
    print("Subtraction is:", a-b)
elif ch=='*':
    print("Multiplication is:", a*b)
elif ch=='/':
    print("Division is:", a/b)
else:
    print("Invalid Input")