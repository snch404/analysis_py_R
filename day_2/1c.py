def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
l=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    num=int(input("Enter element: "))
    l.append(num)
def gcd_num(l):
    n=gcd(l[0], l[1])
    for i in range(2,len(l)):
        n=gcd(n,l[i])
    return n
print("GCD of the list is:", gcd_num(l))