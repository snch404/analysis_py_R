import numpy as np

# 1. Take dimensions from the user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# 2. Take all integer elements from the user
print(f"Enter {rows * cols} integer elements (row-wise):")
elements = [int(input()) for _ in range(rows * cols)]

# Create NumPy matrix m
m = np.array(elements).reshape(rows, cols)
print("\nOriginal matrix (m):\n", m)

# 3. Sort elements in each row (axis=1)
n = np.sort(m, axis=1)
print("\nRow-wise sorted matrix (n):\n", n)

# 4. Sort elements in each column (axis=0)
p = np.sort(n, axis=0)
print("\nColumn-wise sorted matrix (p):\n", p)

# 5. Ask user which statistical operation to perform
print("\nWhich statistical operation do you want to perform?")
print("Options: min, max, range, percentile70, mean, median, variance, std")
choice = input("Enter your choice: ").lower()

# 6. Perform the selected operation directly on the matrix
if choice == "min":
    result = np.min(p)
elif choice == "max":
    result = np.max(p)
elif choice == "range":
    result = np.max(p) - np.min(p)
elif choice == "percentile70":
    result = np.percentile(p, 70)
elif choice == "mean":
    result = np.mean(p)
elif choice == "median":
    result = np.median(p)
elif choice == "variance":
    result = np.var(p)
elif choice == "std":
    result = np.std(p)
else:
    result = "Invalid choice"

# 7. Display result
print(f"\nResult of {choice}: {result}")
