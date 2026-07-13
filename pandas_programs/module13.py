import pandas as pd

df = pd.DataFrame({
    "Category": ["A", "B", "A", "C", "B"],
    "Sales": [100, 200, 150, 300, 250],
    "Profit": [10, 20, 15, 30, 25]
})

# # dataset structure
# print(df.info())

# # univariate
# print(df["Sales"].describe())

# # bivariate
# print(df.groupby("Category")["Sales"].mean())

# correlation
print(df.corr(numeric_only=True))
# print(df.corr("kendall"))

# insights
# print(df.groupby("Category")["Sales"].sum())