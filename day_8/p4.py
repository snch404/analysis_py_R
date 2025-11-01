import re

# Open the source file in read mode
with open("test.txt", "r") as src:
    lines = src.readlines()

# Open the destination file in write mode
with open("dest.txt", "w") as dest:
    for line in lines:
        # Check if line starts with 'This' using regex
        if re.match(r"^This", line):
            # Replace 'This' with 'That'
            new_line = re.sub(r"^This", "That", line)
            dest.write(new_line)
