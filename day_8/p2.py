import re

filename = input("Enter the Python file name: ")
pattern = re.compile(r'\b(def|for)\b')
count = 0
file = open(filename, 'r')
for line in file:
    if pattern.search(line):
        count += 1

print(f"Number of lines containing 'def' or 'for': {count}")
