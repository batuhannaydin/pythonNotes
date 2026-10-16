import pandas as pd

df1 = pd.read_csv("7-concat_data1.csv")
print(df1)
print("******************************************************")

df2 = pd.read_csv("7-concat_data2.csv")
print(df2)
print("******************************************************")

# Concat 
dfConcat = pd.concat([df1, df2], ignore_index = True)
print(dfConcat)
print("******************************************************")


# Merge , kesişen indextekileri birleştirir
dfMerge1 = pd.read_csv("7-merge_data1.csv")
print(dfMerge1)
print("******************************************************")

dfMerge2 = pd.read_csv("7-merge_data2.csv")
print(dfMerge2)
print("******************************************************")

# Merge - outer join, tum verileri getirir, eslesmeyen yerlere NaN deger verir
dfMergedOuter = pd.merge(dfMerge1, dfMerge2, on = "Employee_ID", how = 'outer')
print(dfMergedOuter)
print("******************************************************")

# Merge - left join, 1. tablonun tum verileri getirir, getirilenlerle alakalı bilgi 2.sinde varsa getiriyor yoksa nan veriyor
dfMergedLeft = pd.merge(dfMerge1, dfMerge2, on = "Employee_ID", how = 'left')
print(dfMergedLeft)
print("******************************************************")

# Merge - right join, 2. tablodaki tum verileri getirir, getirilenlerle alakalı bilgi 1.sinde varsa getiriyor yoksa nan veriyor
dfMergedRight = pd.merge(dfMerge1, dfMerge2, on = "Employee_ID", how = 'right')
print(dfMergedRight)
print("******************************************************")

# Merge - Inner join, iki tabloda da kesişen idli verileri getirir
dfMergedInner = pd.merge(dfMerge1, dfMerge2, on = 'Employee_ID', how = 'inner')
print(dfMergedInner)
print("******************************************************")
