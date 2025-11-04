# (i) Initialize two sets
s1 = set()
s2 = set()

# (ii) Take input from the user
n1 = int(input("Enter number of elements for set s1: "))
for i in range(n1):
    val = int(input(f"Enter element {i+1} for s1: "))
    s1.add(val)

n2 = int(input("Enter number of elements for set s2: "))
for i in range(n2):
    val = int(input(f"Enter element {i+1} for s2: "))
    s2.add(val)

print("\nSet s1:", s1)
print("Set s2:", s2)

# (iii) Ask user which operation to perform
print("\nChoose a set operation to perform:")
print("1. Union")
print("2. Intersection")
print("3. Set Difference (s1 - s2)")
print("4. Symmetric Difference")

choice = int(input("Enter your choice (1-4): "))

# (iv) Perform the chosen operation
if choice == 1:
    result = s1.union(s2)
    operation = "Union"
elif choice == 2:
    result = s1.intersection(s2)
    operation = "Intersection"
elif choice == 3:
    result = s1.difference(s2)
    operation = "Set Difference (s1 - s2)"
elif choice == 4:
    result = s1.symmetric_difference(s2)
    operation = "Symmetric Difference"
else:
    print("Invalid choice.")
    exit()

# Display result
print(f"\nResult of {operation}:", result)
