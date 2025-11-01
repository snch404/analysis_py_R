# Finding the roots of a quadratic equation
#     Take the coefficients a, b, and c of a quadratic equation ax^2+bx+c=0 from the user.
#     Find the roots (could be real & equal, real & unequal, or complex conjugate). 
#     Display the roots to the user in a proper format. 
#     Make at least 3 attempts to input the values of a, b, and c such that all the above three cases arise.
from math import *
a= float(input("Enter coefficient a: "))
b= float(input("Enter coefficient b: "))
c= float(input("Enter coefficient c: "))
d= b**2 - 4*a*c
if d > 0:
    r1 = (-b + sqrt(d)) / (2 * a)
    r2 = (-b - sqrt(d)) / (2 * a)
    print("The roots are real and unequal:", r1, "and", r2)
elif d == 0:
    r = -b / (2 * a)
    print("The roots are real and equal:", r, "and", r)
else:
    real_part = -b / (2 * a)
    imaginary_part = sqrt(-d) / (2 * a)
    r1 = complex(real_part, imaginary_part)
    r2 = complex(real_part, -imaginary_part)
    print("The roots are complex conjugates:", r1, "and", r2)