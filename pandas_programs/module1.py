import pandas as pd
s = pd.Series([34,50,33,45,64],index=["a","b","c","d","e"])
# print(s)
# print(s["d"])
# s = s+5
# print(s)
# s=s*10
# print(s)
# print(s.mean())

data = {
    "Name": ["Amit", "Neha", "Raj"],
    "Age": [25, 30, 28],
    "Score": [85, 90, 88]
}
df = pd.DataFrame(data)
print(df)
# print(df.columns)
# print(df.index)
# print(df["Name"])
# # df.rename(columns={"Name":"Student Name","Score":"Total"})
# # print(df)
# df.rename(columns={"Name":"Student Name","Score":"Total"},inplace=True)
# print(df)
df.index =["a","b","c"]
print(df)