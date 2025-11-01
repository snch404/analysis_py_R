import pandas as pd

# --------------------------------------------------
# 1️⃣ Create a Series from a dictionary
# --------------------------------------------------
data_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
series1 = pd.Series(data_dict)
print("Original Series:")
print(series1)
print("-" * 60)

# --------------------------------------------------
# 2️⃣ Create another Series with custom index order
# --------------------------------------------------
series2 = pd.Series(data_dict, index=['d', 'b', 'e', 'a'])
print("New Series with custom index ['d', 'b', 'e', 'a']:")
print(series2)
print("-" * 60)

# --------------------------------------------------
# 3️⃣ Check for null and non-null values
# --------------------------------------------------
print("Check for NULL values (isnull):")
print(series2.isnull())
print("\nCheck for NOT NULL values (notnull):")
print(series2.notnull())
print("-" * 60)

# --------------------------------------------------
# 4️⃣ Create a DataFrame from dictionary of marks
# --------------------------------------------------
data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['AAA', 'BBB', 'CCC', 'DDD', 'EEE'],
    'Physics': [56, 70, 90, 65, 96],
    'Chemistry': [57, 70, 80, 70, 97],
    'Mathematics': [58, 70, 70, 50, 98]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("-" * 60)

# --------------------------------------------------
# 5️⃣ Add Total and Average columns
# --------------------------------------------------
df['Total'] = df[['Physics', 'Chemistry', 'Mathematics']].sum(axis=1)
df['Average'] = df['Total'] / 3

# --------------------------------------------------
# 6️⃣ Add Grade column based on Average
# --------------------------------------------------
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

print("DataFrame with Total, Average, and Grade:")
print(df)
