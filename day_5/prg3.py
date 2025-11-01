class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # to print object
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # addition between two objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # subtraction between two objects
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # multiplication with integer
    def __mul__(self, num):
        return Point(self.x * num, self.y * num)

    # true division with integer
    def __truediv__(self, num):
        return Point(self.x / num, self.y / num)

    # floor division with integer
    def __floordiv__(self, num):
        return Point(self.x // num, self.y // num)

    # modulus with integer
    def __mod__(self, num):
        return Point(self.x % num, self.y % num)

    # power of object
    def __pow__(self, n):
        return Point(self.x ** n, self.y ** n)

    # comparisons
    def __lt__(self, other):
        return (self.x + self.y) < (other.x + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return (self.x + self.y) > (other.x + other.y)


# ---------- Main Program ----------
p1 = Point(41, 50)
p2 = Point(2, 3)

print("The first object is:", p1)
print("The second object is:", p2)

print("The sum of", p1, "and", p2, "is", p1 + p2)
print("The difference of", p1, "and", p2, "is", p1 - p2)

print("The product of", p1, "and 5 is", p1 * 5)
print("The division of", p1, "and 5 is", p1 / 5)
print("The integer division of", p1, "and 5 is", p1 // 5)
print("The modulus of", p1, "and 5 is", p1 % 5)
print("The Power of 3 of", p2, "is", p2 ** 3)

print()
print(p1, "=", p2, "is", p1 == p2)
print(p1, ">=", p2, "is", (p1 > p2) or (p1 == p2))
print(p1, "<=", p2, "is", (p1 < p2) or (p1 == p2))
print(p1, ">", p2, "is", p1 > p2)
print(p1, "<", p2, "is", p1 < p2)