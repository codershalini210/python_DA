import pandas as pd 
df = pd.DataFrame({
    "Date": ["2023-01-03","2024-01-01","2024-01-01",
             "2023-01-03", "2024-01-02", "2024-01-03","2024-01-04"],
    "Sales": [100, 150,250,452, 200,250,120]
})
# print(df["Date"])
df["Date"] = pd.to_datetime(df["Date"])
# print(df.groupby(by="Date").sum().sort_values(by="Sales",ascending=False).head(1))

# print(df["Date"])
# print(df[df["Date"]=="2024-01-01"])
# print(df[(df["Date"]>="2024-01-01") & (df["Date"]<="2024-01-03")])
df1 = df.set_index("Date")
# print(df1.resample("ME").sum())
print(df1["Sales"].rolling(window=2).sum())
# print(df)
# print("------------------\n",df1)
# print(df1.sort_index(ascending=False).head(3))