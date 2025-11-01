#Find out the sum of the digits of a number provided as command line argument.
import sys
def sod(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
if len(sys.argv) != 2:
    print("Improper number of arguments.")
    sys.exit(1)
number = sys.argv[1]
digit_sum = sod(int(number))
print("The sum of the digits is:", digit_sum)