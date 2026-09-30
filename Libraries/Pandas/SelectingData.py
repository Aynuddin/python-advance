import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Alex", "David"],
    "Age": [25, 30, 28],
    "Country": ["India", "USA", "UK"]
})
# single selecting data full column value
data = df["Name"]
print(data)
# selecting mutiple data
mul_data = df[["Name","Age"]]
print(mul_data)
# using loc: it is label based
# getting specific value
loc_data = df.loc[0,"Name"]
print(loc_data)
# Select specific rows and columns
spec_data = df.loc[0:1,["Name","Age"]]
print(spec_data)
# complete row
print(df.loc[1])

# using iloc : it is integer based access
# for column specific value
sp_val = df.iloc[1,2]
print(sp_val)

# for spec column index all row values
data_spc_col = df.iloc[:,0]
print(data_spc_col)
# first two column each row first value
first_two_col = df.iloc[0,0:2]
print(first_two_col)
# first two col all rows values
first_tow_row_allValues= df.iloc[:,0:2]
print(first_tow_row_allValues)

# Selecting rows with iloc
f1_row_data = df.iloc[0]
print(f1_row_data)