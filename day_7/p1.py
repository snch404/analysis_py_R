import random

# Create a list of size 20 with random numbers from 1 to 9 (using simple loop)
n = []
i = 0
while i < 20:
    num = random.randint(1, 9)
    n.append(num)
    i += 1

print("Original List:", n)

# (a) Function to find unique elements (appear only once)
def find_unique_elements(lst):
    result = [x for x in lst if lst.count(x) == 1]
    return result

# (b) Function to find duplicates with their occurrences
def find_duplicates(lst):
    duplicates = {}
    for x in set(lst):  # check only unique values
        count = lst.count(x)
        if count > 1:
            duplicates[x] = count
    return duplicates

# (c) Function to create a list of all unique elements (no repetition, keep order)
def unique_list(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result


# Test
print("Unique elements (only once):", find_unique_elements(n))
print("Duplicate elements with counts:", find_duplicates(n))
print("Unique list (all elements once):", unique_list(n))
