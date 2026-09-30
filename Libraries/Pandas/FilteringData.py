# Filtering Data:
# filtering the data from DataFrame by applying the condition and keeping only rows value where the condition
# is True

import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Alex", "David", "Sarah", "Mike"],
    "Age": [25, 30, 28, 22, 35],
    "Country": ["India", "USA", "UK", "India", "USA"],
    "Salary": [50000, 60000, 55000, 40000, 70000]
})

# filter the row whose Age is greater than 28
customer_data = df[df["Age"] > 28]
print(customer_data)

# filter between using (&)
cus_data = df[(df["Name"] == "David") & (df["Age"] == 28)]
print(cus_data)

# check item exists then give row
cust_items = df[df["Country"].isin(["India"])]
print(cust_items)

# check except this value row , give all other row
except_val_row_other_row = df[~df["Country"].isin(["India","UK"])]
print(except_val_row_other_row)