from math import *
def check_range(x):
    if 1 <= x <= 255:
        return 1
    else:
        return 0
def find_n(x):
    return log2(x)
while True:
    try:
        x = int(input("Number of registers in the CPU: "))
        if check_range(x):
            n = find_n(x)
            print("The number of bits for the Register field in the Instruction format is:", ceil(n))
            break
        else:
            print("Input out of range. Please enter a number between 1 and 255.")
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 255.")