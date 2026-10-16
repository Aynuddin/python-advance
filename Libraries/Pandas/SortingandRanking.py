# Sorting and Ranking : it helps to organize data and identify the highest,lowest,newest and oldest records.
# These operations are useful when doing ETL Testing,Data Engineering and Data Quality Engineering.

import pandas as pd

df = pd.DataFrame({
    "OrderID": [103, 101, 104, 102],
    "Customer": ["Amit", "Rahul", "Priya", "Neha"],
    "Amount": [3000, 5000, 4000, 4000]
})

# Use sort_values() when you want to sort by columns such as Amount or OrderDate.
# Use sort_index() when you want to organize rows by their index labels.

# sort by values :  we can sort the records by its column value
# by default it is ascending
df_sort = df.sort_values("Amount",ascending=False)
#print(df_sort)

# sort by multiple columns :
# Example
sort_by_mul_columns = df.sort_values(["Customer","Amount"], ascending=[True,False])
#print(sort_by_mul_columns)

# sort_index(ascending=True/False) : this will organize data based on their order
sort_by_index = df.sort_index(ascending=False)
#print(sort_by_index)

# nlargest(no of rows,based on column-name) : it will give from top but column-name need to choose number type
# nsmallest(no of rows,based on column-name): it will give from bottom but column-name need to choose number type
# ETL use case: Identify the top 10 sales transactions or investigate unusually small transactions
nlargest_rows = df.nlargest(2,"Amount")
#print(nlargest_rows)
nsmallest_rows = df.nsmallest(2,"OrderID")
#print(nsmallest_rows)

# rank() — Assign a rank to each row
#df["Rank"] = df["Amount"].rank(ascending=True)


# if two rows have same value then the default ranking method will give the average of their tied positions.
# here method you can give, min,dense or first
df["Rank"] = df["Amount"].rank(
    ascending=False,
    method="dense"
)
#print(df)

df_Amount = df.loc[1,"Amount"]
print(df_Amount)

