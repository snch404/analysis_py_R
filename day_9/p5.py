import numpy as np

# Step 1: Take user input to create a 4x3 matrix
rows, cols = 4, 3
print(f"Enter {rows * cols} integer elements for a {rows} x {cols} matrix (row-wise):")

elements = []
for i in range(rows * cols):
    val = float(input(f"Element {i + 1}: "))
    elements.append(val)

m = np.array(elements).reshape(rows, cols)
print("\nOriginal Matrix (m):\n", m)

# Step 2: Find the column mean
cm = np.mean(m, axis=0)
print("\nColumn Mean (cm):\n", cm)
print("Shape of column mean:", cm.shape)

# Step 3: Demean the columns (subtract column mean from each element)
demeancol = m - cm
print("\nDemeaned Matrix (m - cm):\n", demeancol)

# Step 4: Explain Broadcasting
print("\n--- Broadcasting Explanation ---")
print(f"Shape of m        : {m.shape}")
print(f"Shape of cm       : {cm.shape}")
print("\nTo perform m - cm, NumPy applies the following broadcasting rule:")
print("→ Since cm has shape (3,), it is treated as (1,3)")
print("→ NumPy replicates it across 4 rows to match m’s shape (4,3)")
print("→ Element-wise subtraction is then performed column-wise.")
