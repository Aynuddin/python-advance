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
#print(mdf)

# concat() : used to combine two or more DataFrame's along rows and columns
# if you want vertical concating then used axis=0 and horizontal then axis=1
# Syntax = pd.concat([df1,df2],axis=0,ignore_index=True)
# Example :
df1 = pd.DataFrame({
    "CustId":[101,102],
    "Name":["Ayn","Uddin"]
})

df2 = pd.DataFrame({
    "CustId":[103,104],
    "Name":["Sham","Ram"],
    "Salary":[2000,3000]
})
df3 = pd.DataFrame({
    "Country": ["India", "UK"],
    "Salary":[2000,3000]
})

# vertical conacting
con_df = pd.concat([df1,df2],axis=0,ignore_index=True)
#print(con_df)

# horizontal concat
hor_df = pd.concat([df1,df3],axis=1,ignore_index=False)
#print(hor_df)

# without passing axis also we can able to concat
without_axis = pd.concat([df1,df2],ignore_index=True)
print(without_axis)

# Date Operations: It helps to extract,filter,compare and calculate dates.
# For example, in an ETL project, you may need to filter orders created in a particular month, calculate delivery time,
# or validate whether a date is in the correct format.
# Convert a column to datetime : pd.to_datetime(df[column_name])

df_do = pd.DataFrame({
    "OrderID": [1, 2, 3, 4],
    "OrderDate": [
        "2026-01-10",
        "2026-02-15",
        "2026-02-25",
        "2026-03-05"
    ],
    "DeliveryDate": ["2026-01-04", "2026-01-12", "2026-01-15"],
    "Amount": [1000, 2000, 3000, 4000]
})
# here it will convert the field OrderDate as date field
# If invalid date values the add this : errors="coerce", Invalid dates become NaT, so we find missing date easily
# using isna()
df_do["OrderDate"] = pd.to_datetime(df_do["OrderDate"], errors="coerce")
df["DeliveryDate"] = pd.to_datetime(df["DeliveryDate"], errors="coerce")

# We can Extract year, month, and day by using .dt accessor: days,month,year etc.
# for example : df["Month"] = df["OrderDate"].dt.month -> it will return month

# We can also able to do filters in date Filter records by date using condition or(|) and (&)
# Example : (df["OrderDate"] >= "2026-02-01") & (df["OrderDate"] < "2026-03-01") -> here will check only for february
# you can  Calculate the difference between dates to find days or month or year
# first convert both columns to date using to_datetime() then subtract from - to and access using .dt.days or month or yaer
# Example : df["DeliveryDays"] = (df["DeliveryDate"] - df["OrderDate"]).dt.days // to find days

# Sort records by date: we can also do sort by date
# Syntax df = df.sort_values(column-name,ascending=True)

#6 : Handle missing and invalid dates using isna() and notna()
# copy will create separate 
# Get rows with missing OrderDate
invalid_data_df = df[df["OrderDate"].isna()].copy()
# Get rows with non-missing OrderDate
valid_data_df = df[df["OrderDate"].notna()].copy()

