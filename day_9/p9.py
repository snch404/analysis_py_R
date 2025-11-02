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

# Step 1: Create a one-dimensional array-like object (Series)
data = [10, 20, 30, 40]
s = pd.Series(data)
print("Original Series:")
print(s)

# Step 2: Change the index to new labels
s.index = ['d', 'b', 'a', 'c']
print("\nSeries with new index:")
print(s)

# Step 3: Update data points using new indices
s['d'] = 15
s['b'] = 25
print("\nUpdated Series:")
print(s)

# Step 4: Fancy indexing examples
print("\nFancy indexing (select 'a' and 'c'):")
print(s[['a', 'c']])

print("\nFancy indexing (select using index list ['c', 'b', 'd']):")
print(s[['c', 'b', 'd']])
