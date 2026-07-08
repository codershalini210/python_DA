import pandas as pd 
df = pd.read_excel("Basic Excel.xlsx")
print(df.head(2))
# print(df.info())
# print(df.describe())
# print(df["sub3"].describe())
print("shape" ,df.shape)
print("coumns---------------\n",df.columns)
print("dtypes -----------------\n",df.dtypes)