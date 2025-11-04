# Part (a)
from functools import reduce

# Create list with numbers from 0 to 20
numbers = list(range(21))

# (a) Using lambda + filter to print all numbers divisible by both 3 and 5
divisible_by_3_and_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)

# (b) Using lambda + map to find square of each number
squares = list(map(lambda x: x ** 2, numbers))
print("Squares of all numbers:", squares)

# (c) Using lambda + reduce to find product of all numbers from user input
user_list = [int(input("Enter number: ")) for _ in range(5)]
product = reduce(lambda x, y: x * y, user_list)
print("Product of all numbers:", product)
