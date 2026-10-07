# Reading Data : It is used in Pandas to extracting data from files,api and load it to DF.
# Example: Csv file, JSON file and Excel file

import pandas as pd

# read csv
csv_df = pd.read_csv("customers.csv")
# #print(csv_df)
#
# # Practice questions
# # first 5 rows
# first_five_row = csv_df.head(5)
# #print(first_five_row)
# # number of rows and columns
# no_rows_cols = csv_df.shape
# print(no_rows_cols)
# # column names
# cols_name = csv_df.columns
# print(cols_name)
# # data types
# csv_data_types = csv_df.dtypes
# print(csv_data_types)
#
# # read json
# json_csv = pd.read_json("customer.json")
# #print(json_csv)
#
# spec_col_df = json_csv["Name"]
# #print(spec_col_df)
# # remove row which one row value missing
# remove_full_row_missing_value = spec_col_df.dropna()
# #print(remove_full_row_missing_value)
# Questions :
# Find all customers whose Age is missing
# isna() will filter out those rows which age is missing and return those rows
missing_df = csv_df[csv_df["Age"].isna()]
print(missing_df)

# Find all customers from India
cus_india = csv_df[csv_df["Country"] == "India"]
#print(cus_india)

# Find all customers whose PurchaseAmount is greater than 2000
amt_greater_than_2000 = csv_df[csv_df["PurchaseAmount"] > 2000]
#print(amt_greater_than_2000)

# Count how many missing values exist in each column.
# here isna() will give how many and sum will plus it for each row
missing_count = csv_df.isna().sum()
#print(missing_count)

# Remove all rows where either CustomerID OR Name is missing.
remove_row = csv_df.dropna(subset=["CustomerID","Name"])
#print(remove_row)

# Replace missing Country values with "Unknown" without removing the row.
csv_df["Country"] = csv_df["Country"].fillna("Unknown")
#print(csv_df)

# reading using excel
excel_data = pd.read_excel("customers.xlsx")
#print(excel_data)