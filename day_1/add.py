import sys
if(len(sys.argv)<3):
    print("Improper no. of arguments")
else:
    a=eval(sys.argv[1])
    b=eval(sys.argv[2])
    c=a+b
    print("Sum of",a,"&",b,"is:",c)