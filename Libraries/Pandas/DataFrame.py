# DataFrame:-> It is two-dimensional labeled data structure.
# A collection of series
# Think of it like an Excel table or database table:
# A DataFrame has Rows,Columns,Row Index and Columns name

# create DataFrame using single dictionaries
import pandas as pd

data = {
    "name":["Ayn","Uddin"],
    "age":[25,35],
    "Status":[True,False]
}
df = pd.DataFrame(data)
print(df)

# Creating DataFrame from List of Dictionaries
data_lidict = [
    {"name":"Ayn","age":32},
    {"name":"Uddin","age":52}
]
df_list = pd.DataFrame(data_lidict)
print(df_list)

# shape , it will give how many rows and column
print(df_list.shape)
# size
print(df_list.size)
# dtypes:Shows the data type of each column.
print(df_list.dtypes)

# head() -> first element
print(df_list.head())
# tail()
print(df_list.tail())

# info() -> it will give all information of dataframe
print(df_list.info())

# describe -> statical information
print(df_list.describe())

# Flow: Raw Data->DataFrame->Check schema-> Check nulls->Clean Data->Transform Data->Load
# You receive a DataFrame containing 20 columns and 1 million records.
# What would you check before transformation?
# Before starting transformation, which DataFrame methods/attributes would you use to understand the dataset?
# ans: Before transforming a large dataset, I would perform initial data profiling to understand its structure,
# schema and data quality.
# I would use shape to verify its dimensions,
# head() to inspect sample records,
# info() to check column types and non-null counts,
# dtypes to validate data types,
# and describe() to understand the numerical columns.