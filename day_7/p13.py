# Create first list: roll numbers 1 to 25
roll_numbers = list(range(1, 26))

# Read names from a file
# (Assume the file 'names.txt' contains 25 names, one per line)
with open("names.txt", "r") as file:
    names = [line.strip() for line in file.readlines()]

# Combine the two lists into a dictionary
students = dict(zip(roll_numbers, names))

# Display the dictionary
print("Roll No - Name mapping:\n")
for roll, name in students.items():
    print(f"{roll}: {name}")
