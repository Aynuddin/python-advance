# Writing Data to csv means save the processed data

import pandas as pd
df = pd.DataFrame({
    "CustomerID": [101, 102, 103,101],
    "Name": ["John", "Alex", "Sarah","John"],
    "Country": ["India", "USA", "UK","India"]
})

# write data to csv
save_data = df.to_csv("employee.csv", index=False)
print(save_data)

# only index data
df.to_csv("columns.csv", columns=["Name","Country"],index=False)

### HANDLING DUPLICATES======
# find duplicate
df_dup = df[df.duplicated()]
print(df_dup)
# find dupliacte based on column df.duplicated(subset=["CustomerID"])

# drop or remove duplicate based on column by default keep first, if you tell keep = last, it will keep last
rem_dup = df.drop_duplicates(subset=["CustomerID"])
print(rem_dup)

# drop all duplicates
rem_all_sup = df.drop_duplicates()
print(rem_all_sup)