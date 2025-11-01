import numpy as np

# Create a NumPy array of strings
arr = np.array(['Python', 'NumPy', 'AI', 'Data'])

print("Original Array:")
print(arr)

# Insert a space between each character of every string element
spaced_arr = np.char.join(' ', arr)

print("\nArray after inserting spaces between characters:")
print(spaced_arr)
