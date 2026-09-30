# Cleaning Data : it will identifying and correcting problems in raw data before using it for data analysis,
#                  transforming and loading to the target system.
import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Alex", "David", "Sarah"],
    "Age": [25, None, 28, None],
    "Country": ["India", "USA", None, "India"],
    "Salary": [50000, 60000, None, 45000]
})

#print(df)

# isna() :  this method will print the df itself but where None/NaN/NaT replace with True other False
# if you want any operations like sum or count etc, then use method like sum() or count or assert
# so in df it will fill True where None/NaN/NaT
# df.isna().sum() : this will give how many missing number or element
is_missing_val = df.isna()
print(is_missing_val)
# so if you want to check how many then sum() it
# it will give each column how many missing
sum_mis = df.isna().sum()
print(sum_mis)

# it will give which column missing means null value is True
print(df.isna().any())
# it will give True , if in df any missing number or element
print(df.isna().any().any())

# for assertions check like this
# for quality data engineer : assert df["Country"].isna() == 0
is_find = df["Country"].isna().sum() == 0
print(is_find)

# notna() : it is the opposite of isna, here NaN/None/NaT replace with Flase and rest True in df
# but if anything  want like sum or count, then use method like sum or count or assert
# df.notna().sum(), it will give each column how many number or element

notna_df = df.notna()
print(notna_df)

# here we can check which column wise no missing element
col_wise_missing = df.notna().sum()
print(col_wise_missing)

# filter the column not display if missing number is there
# if column contains like NaN/None/NaT
# one more way df[df["Age"].notna()]
not_missing_age = df[~df["Age"].isna()]
print(not_missing_age)

# missing age print the row
missing_age = df[df["Age"].isna()]
print(missing_age)

# fillna(data): this will fill the missing value
# it will fill all in df where NaN/None/NaT
df["Age"] = df["Age"].fillna(20)
df["Country"] = df["Country"].fillna("Uk")
print(df)

# dropna() : Instead of filling missing values, we can remove rows containing missing values.
df1 = df.dropna()
print(df1)
# here also specific column based removing rows
# suppose if one column 3 row missing element then it will remove only third row
df2 = df.dropna(subset="Name")
print(df2)

# more than one column you can check
df3 = df.dropna(subset=["Salary", "Name", "Age"])
print(df3)

# Cheat sheet

# Check missing values
df.isna()

# Count missing values
df.isna().sum()

# Check non-missing values
df.notna()

# Find missing Age
df[df["Age"].isna()]

# Find valid Age
df[df["Age"].notna()]

# Fill missing values
df["Age"] = df["Age"].fillna(0)

# Fill with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill categorical missing values
df["Country"] = df["Country"].fillna("Unknown")

# Remove rows with any missing value
df.dropna()

# Remove rows where specific column is missing
df.dropna(subset=["Name"])

print("=========")
print(df[df["Age"].notna()])
