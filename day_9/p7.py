import numpy as np

# Create two NumPy arrays
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([15, 20, 25, 40])

print("Array 1:", arr1)
print("Array 2:", arr2)
print("-" * 50)

# Element-wise comparisons
print("Equal (arr1 == arr2):\n", np.equal(arr1, arr2))
print("Not Equal (arr1 != arr2):\n", np.not_equal(arr1, arr2))
print("Greater Equal (arr1 >= arr2):\n", np.greater_equal(arr1, arr2))
print("Greater (arr1 > arr2):\n", np.greater(arr1, arr2))
print("Less (arr1 < arr2):\n", np.less(arr1, arr2))
