import re

txt = ' Hello hello students of CSE2025'

# 1) Find all lower case characters alphabetically between "a" and "m"
lower_a_m = re.findall(r'[a-m]', txt)

# 2) Find all lowercase characters excluding [a-m]
lower_not_a_m = re.findall(r'[n-z]', txt)

# 3) Find all digit characters
digits = re.findall(r'\d', txt)

# 4) Search for a sequence that starts with "he", followed by two (any) characters, and an "o"
he_two_any_o = re.findall(r'he..o', txt)

# 5) Search for a sequence that starts with "he", followed by 0 or more (any) characters, and an "o"
#    Use non-greedy quantifier to avoid overmatching
he_zero_or_more_any_o = re.findall(r'he.*?o', txt)

# 6) Search for a sequence that starts with "he", followed by 1 or more (any) characters, and an "o"
#    Use non-greedy quantifier to get the shortest match to 'o'
he_one_or_more_any_o = re.findall(r'he.+?o', txt)

# 7) Search for a sequence that starts with "He", followed exactly 2 (any) characters, and an "o"
He_two_any_o = re.findall(r'He..o', txt)

print("Lowercase [a-m]:", lower_a_m)
print("Lowercase excluding [a-m]:", lower_not_a_m)
print("Digits:", digits)
print('Pattern "he..o":', he_two_any_o)
print('Pattern "he.*?o":', he_zero_or_more_any_o)
print('Pattern "he.+?o":', he_one_or_more_any_o)
print('Pattern "He..o":', He_two_any_o)
