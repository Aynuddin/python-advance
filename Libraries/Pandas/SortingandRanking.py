# Sorting and Ranking : it helps to organize data and identify the highest,lowest,newest and oldest records.
# These operations are useful when doing ETL Testing,Data Engineering and Data Quality Engineering.

import pandas as pd

df = pd.DataFrame({
    "OrderID": [103, 101, 104, 102],
    "Customer": ["Amit", "Rahul", "Priya", "Neha"],
    "Amount": [3000, 5000, 1000, 4000]
})

# sort by values
# by default it is ascending
df_sort = df.sort_values("Amount",ascending=False)
print(df_sort)