# Creating a dictionary with key-value pairs
student = {
    "name": "Sanchayan",
    "age": 20,
    "branch": "CSE",
    "year": 2
}

# (i) Print the value of a dictionary item for a specific key
print("Value for key 'branch':", student["branch"])

# (ii) Add an item to a dictionary by assigning a value to a new key
student["college"] = "Heritage Institute of Technology"
print("After adding new item:", student)

# (iii) Remove an element from a dictionary
student.pop("year")
print("After removing 'year':", student)

# (iv) Change the value of a dictionary element by referring to its key
student["age"] = 21
print("After changing value of 'age':", student)

# (v) Iterate through dictionary keys one by one
print("Iterating through keys:")
for key in student:
    print(key, ":", student[key])

# (vi) Find the length of the dictionary
print("Length of dictionary:", len(student))
