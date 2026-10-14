# Pandas Data Transformation :  we can transformed data before loading it into a target table

# using add or creating new column , apply() and map()

import pandas as pd
from pandas import merge

df = pd.DataFrame({
    "OrderID": [101, 102, 103],
    "Amount": [1000, 2000, 3000],
    "Country":["IN","USA","UK"]
})

# i will add one column call Tax: here we will cut tax on 0.18 %
# creating column
df["Tax"] = df["Amount"] * 0.18
#print(df)

# apply() : it is function used to apply to a values in Pandas Series or rows and columns of DataFrame.
# apply() function need to pass one function parameter
# Example: Apply a discount rule
#Business requirement:
#- Amount greater than or equal to 2,000 → 10% discount.
# - Amount below 2,000 → 5% discount.

def calculate(amount):
    if amount >= 2000:
        return amount * .10
    else:
        return amount * 0.05

df["Discount"] = df["Amount"].apply(calculate)
#print(df)

# map() : used to transform the values in Series(only single column)
# Requirement : change the country code to full country name
# using dictionary we can do that

mapping_name = {
    "IN":"India",
    "USA":"United States of America",
    "UK":"United Kingdom"
}

df["Country"] = df["Country"].map(mapping_name);
#print(df)

dt = pd.DataFrame({
    "OrderId":[1,2,3],
    "Status":[1,2,3]
})

# Requirement : changing the int number to string like
# 1: pending 2: shipped 3: delivered
mapping_status={
    1:"Pending",
    2:"Shipped",
    3:"Delivered"
}
dt["Status"] = dt["Status"].map(mapping_status)
#print(dt)

# merge(): Here we can combine data from two tables using the common column
# like joins it will work
# syntax : pd.merge(df1,df2,on="CutsId", how=""inner")
customers = pd.DataFrame({
    "CustId":[101,102,103],
    "Name":["Ayn","Sham","Gaib"]
})
orders = pd.DataFrame({
    "OrderId":[10,11,12],
    "CustId":[101,102,103],
    "Status":["Pending","Shipped","Delivered"]
})
mdf = pd.merge(customers,orders,on="CustId",how="inner")
print(mdf)

# concat() : used to combine the two DataFrame


