# Accept number of elements
n = int(input("Enter number of elements in the list: "))

# Create list with user input
lst = []
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    lst.append(val)

# Display the list
print("\nList entered:", lst)

# Accept the number to check
num = int(input("Enter the number to find indices of (if repeated): "))

# Find all indices where num occurs
indices = [i for i, x in enumerate(lst) if x == num]

# Display result
if len(indices) > 1:
    print(f"The number {num} occurs multiple times at indices:", indices)
elif len(indices) == 1:
    print(f"The number {num} occurs only once at index:", indices[0])
else:
    print(f"The number {num} does not occur in the list.")
