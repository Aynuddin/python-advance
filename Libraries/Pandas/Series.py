# Pandas : It is a python library used for working with structured or tabular data.
# It is commonly used for :
#  Reading data from json/excel/csv , Cleaning data, Transforming data, Filtering data, Aggregating data
#  Preparing data for ETL pipelines
#  Data Analysis
# for importing pandas use:  import pandas as pd

# Topic1 : Series -> It is one dimensional labeled data structure
# create series
import pandas as pd

data = pd.Series([1,2,3,4,5])
print(data)
# index position based search
print(data.iloc[2])
#loc-> label based search
print(data.loc[2])
str_data = pd.Series(["Ayn","Uddin","Sham","Kam"])
print(str_data)

# custom index also you can give
names = pd.Series(
    ["John", "Alex", "David"],
    index=["A", "B", "C"]
)
print(names["A"])
# freq of each element
freq = pd.Series(["India","USA","UK","India","UK"])
print("Freq of each ele :",freq.value_counts())