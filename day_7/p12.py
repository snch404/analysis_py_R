# Create a list
lst = [100, 50, 65, 82, 23]

# Sort the list using customized key function
lst.sort(key=lambda n: abs(n - 50))

# Display the result
print("Result list:", lst)
