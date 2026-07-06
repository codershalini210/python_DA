import pandas as pd
# df = pd.read_csv("electronics.csv")
# print(df)
df = pd.read_excel("Basic Excel.xlsx")
# print(df.head(3))
print("-----------------------")
print(df[df["result"]=="Pass"])

print("-----------------------")
print(df[df["result"]!="Pass"])
# print(df.tail())
# pip install openpyxl