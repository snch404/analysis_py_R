# import pandas as pd

# # Step 1: Create a one-dimensional array-like object using Pandas Series
# data = pd.Series([10, 20, 30, 40])
# print("Original Series:")
# print(data)
# print("-" * 50)

# # Step 2: Change the index
# data.index = ['d', 'b', 'a', 'c']
# print("Series with New Index:")
# print(data)
# print("-" * 50)

# # Step 3: Update a data point using new index
# data['b'] = 25
# print("Series after updating index 'b' to 25:")
# print(data)
# print("-" * 50)

# # Step 4: Fancy indexing examples
# # Fancy indexing allows selecting multiple elements at once
# print("Fancy Indexing Examples:")

# print("Values at index positions ['d', 'a']:\n", data[['d', 'a']])
# print("\nValues at index positions ['c', 'b', 'd']:\n", data[['c', 'b', 'd']])
# print("\nSliced values from 'b' to 'c':\n", data['b':'c'])

import pandas as pd

# Step 1: Create Series with default index
data = pd.Series([10, 20, 30, 40])
print("Original Series:")
print(data)
print("-" * 50)

# Step 2: Change index safely
data = data.set_axis(['d', 'b', 'a', 'c'])
print("Series with New Index:")
print(data)
print("-" * 50)

# Step 3: Update a value
data.loc['b'] = 25
print("After updating index 'b' to 25:")
print(data)
print("-" * 50)

# Step 4: Fancy indexing
print("Fancy Indexing Examples:")
print("Values at ['d', 'a']:\n", data.loc[['d', 'a']])
print("\nValues at ['c', 'b', 'd']:\n", data.loc[['c', 'b', 'd']])
print("\nSliced from 'b' to 'c':\n", data.loc['b':'c'])
