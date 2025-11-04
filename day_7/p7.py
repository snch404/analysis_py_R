def generate_primes(n):
    count = 0
    num = 2
    while count < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


# Taking user input
n = int(input("Enter the number of prime numbers you want to generate: "))

print(f"First {n} prime numbers:")
for prime in generate_primes(n):
    print(prime, end=" ")
