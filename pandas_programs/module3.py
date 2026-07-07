import pandas as pd

df = pd.read_json("data.json")
print(df.head())
df_True = df #[df["completed"]==True] 
print(df_True)
id = int(input("Enter user id "))

df_7 =df_True[df["userId"]==7]
print(df_7.count())

# df = pd.read_csv("electronics.csv")
# print(df)
# df = pd.read_excel("Basic Excel.xlsx")
# print(df.head(3))
# print("-----------------?------")
# print(df[df["result"]=="Pass"])
# df=df.replace("NaN",0)
# df=df[df["%"]!="Fail"]
# df=df[df["%"].isna()!=True]
# print(df[df["%"]==max(df["%"])])
# print("-----------------------")
# print(df[df["result"]!="Pass"])
# print(df.tail())
# pip install openpyxl
# print(max((df[df["%"]!="fail"].astype(float))))
# print((df[(df["%"]!="Fail")]))
# d= (df[(df["%"]!="Fail")])
# print(d[d["%"]!="NaN"])
# for i in d :
#     print(i)
    # print(i["%"], "its data type ", type(i["%"]))