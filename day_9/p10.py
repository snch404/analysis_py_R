import pandas as pd

# ----- Part 1: Series -----
# Create a Series from a dictionary
data = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
s1 = pd.Series(data)
print("Original Series:")
print(s1)

# Create another Series with custom index order
s2 = pd.Series(data, index=['d', 'b', 'e', 'a'])
print("\nSeries with given index order:")
print(s2)

# Check for null and non-null values
print("\nChecking for null values:")
print(s2.isnull())

print("\nChecking for non-null values:")
print(s2.notnull())

# ----- Part 2: DataFrame -----
# Create DataFrame from a dictionary
marks_data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['AAA', 'BBB', 'CCC', 'DDD', 'EEE'],
    'Physics': [56, 70, 90, 65, 96],
    'Chemistry': [57, 70, 80, 70, 97],
    'Mathematics': [58, 70, 70, 50, 98]
}

df = pd.DataFrame(marks_data)
print("\nOriginal DataFrame:")
print(df)

# Add Total and Average columns
df['Total'] = df['Physics'] + df['Chemistry'] + df['Mathematics']
df['Average'] = df['Total'] / 3

# Add Grade column based on Average
def assign_grade(avg):
    if avg >= 90:
        return 'O'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Average'].apply(assign_grade)

print("\nDataFrame after adding Total, Average, and Grade:")
print(df)
