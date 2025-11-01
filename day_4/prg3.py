try:
    n1,n2=eval(input("Enter two numbers, separated by comma: "))
    result=n1/n2
    print("result is ",result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except SyntaxError:
    print("Comma may be missing")
# except:
#     print("Something wrong in input")
else:
    print("No Exceptions")
# finally:
#     print("The finally clause is executed")