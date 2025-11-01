def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Take input from user
n = int(input("Enter size of list: "))
L = []

print("Enter the elements:")
for _ in range(n):
    L.append(int(input()))

# Find first prime
prime_found = False
for num in L:
    if is_prime(num):
        print("First prime number in list:", num)
        prime_found = True
        break

if not prime_found:
    print("No prime number found in list")
