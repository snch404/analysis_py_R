#By using the concept of default arguments, accept sides of a triangle (for three sides take default values) and check the type of triangle and find out area of the triangle.
def triangle_area(a=3, b=4, c=5):
    s = (a + b + c) / 2  # Semi-perimeter
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Heron's formula
def triangle_type(a=3, b=4, c=5):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Equilateral triangle")
        elif a == b or b == c or a == c:
            print("Isosceles triangle")
        elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            print("Right-angled triangle")
        else:
            print("Scalene triangle")
        print("Triangle area:", triangle_area(a, b, c))
    else:
        print("Not a triangle")

a = int(input("Enter side a: ") or 3)
b = int(input("Enter side b: ") or 4)
c = int(input("Enter side c: ") or 5)
triangle_type(a, b, c)
