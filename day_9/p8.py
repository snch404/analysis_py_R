import numpy as np

# Step 1: Create two 3x3 matrices
A = np.array([[2, 4, 6],
              [1, 3, 5],
              [7, 9, 11]])

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# Step 2: Matrix Addition
add_result = A + B
print("\nMatrix Addition (A + B):\n", add_result)

# Step 3: Matrix Subtraction
sub_result = A - B
print("\nMatrix Subtraction (A - B):\n", sub_result)

# Step 4: Element-wise Multiplication
mul_result = A * B
print("\nElement-wise Multiplication (A * B):\n", mul_result)

# Step 5: Element-wise Division
div_result = A / B
print("\nElement-wise Division (A / B):\n", div_result)

# Step 6: Transpose of Matrices
print("\nTranspose of Matrix A:\n", A.T)
print("\nTranspose of Matrix B:\n", B.T)
