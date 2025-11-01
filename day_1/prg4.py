import sys
if(len(sys.argv)<4):
    print("Improper no. of arguments")
else:
    a=eval(sys.argv[1])
    b=eval(sys.argv[2])
    l=eval(sys.argv[3])
if(a<b):
    print("a<b")
if(a>b):
    print("a>b")
if(a<=b):
    print("a<=b")
if(a>=b):
    print("a>=b")
if(a==b):
    print("a==b")
if(a!=b):
    print("a!=b")
if(a is b):
    print("a is b")
if(a is not b):
    print("a is not b")
if(a in l):
    print("a in l")
if(b in l):
    print("b in l")
if(a not in l):
    print("a not in l")
if(b not in l):
    print("b not in l")