import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:\n", arr1)
print("Shape:", arr1.shape)
print("Dimension:", arr1.ndim)
print("Data Type:", arr1.dtype)
print("-" * 40)

# 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("2D Array:\n", arr2)
print("Shape:", arr2.shape)
print("Dimension:", arr2.ndim)
print("Data Type:", arr2.dtype)
print("-" * 40)

# 3D array
arr3 = np.array([[[1, 2, 3],
                  [4, 5, 6]],
                 [[7, 8, 9],
                  [10, 11, 12]]])
print("3D Array:\n", arr3)
print("Shape:", arr3.shape)
print("Dimension:", arr3.ndim)
print("Data Type:", arr3.dtype)
print("-" * 40)

# Reshaping arrays
# 1D to 2D
reshaped_1D_to_2D = arr1.reshape(5, 1)
print("Reshaped 1D to 2D:\n", reshaped_1D_to_2D)
print("Shape:", reshaped_1D_to_2D.shape)
print("Dimension:", reshaped_1D_to_2D.ndim)
print("-" * 40)

# 2D to 3D
reshaped_2D_to_3D = arr2.reshape(2, 1, 3)
print("Reshaped 2D to 3D:\n", reshaped_2D_to_3D)
print("Shape:", reshaped_2D_to_3D.shape)
print("Dimension:", reshaped_2D_to_3D.ndim)
print("-" * 40)

# 2D to another 2D shape
reshaped_2D_diff = arr2.reshape(3, 2)
print("Reshaped 2D to different shape:\n", reshaped_2D_diff)
print("Shape:", reshaped_2D_diff.shape)
print("Dimension:", reshaped_2D_diff.ndim)
