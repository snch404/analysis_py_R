import numpy as np
import pandas as pd

# i) 1-D array of zeros
zeros = np.zeros(10)
print("i) zeros array:\n", zeros)

# ii) 2-D array of ones (2x5) with dtype=int
ones = np.ones((2, 5), dtype=int)
print("\nii) ones array:\n", ones)

# iii) 2-D array using arange() with start=4, step=4, 3 rows and 5 columns, dtype=float
myarray2 = np.arange(4, 4 + 4 * 3 * 5, 4, dtype=float).reshape(3, 5)
print("\niii) myarray2 array:\n", myarray2)

# iv) Create a Series object using np.tile()
array = np.array([1, 2, 3])
tiled_array = np.tile(array, 3)  # repeats the array 3 times
series = pd.Series(tiled_array)
print("\niv) Series from tiled array:\n", series)
