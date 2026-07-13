# import pandas as pd

# arrays = [
#     ["A", "A", "B", "B"],
#     ["X", "Y", "X", "Y"]
# ]

# index = pd.MultiIndex.from_arrays(arrays, names=("Group", "Subgroup"))

# df = pd.DataFrame({"Value": [10, 20, 30, 40]}, index=index)
# print(df.loc[("A","X")])
# print(df.query("Value > 30"))


import pandas as pd

df = pd.DataFrame({
    "Date": ["2024-01-01", "2024-01-01", "2024-01-02"],
    "City": ["A", "B", "A"],
    "Sales": [100, 200, 150]
})

# Pivot
pivot_df = df.pivot(index="Date", columns="City", values="Sales")

# Melt
melted = pd.melt(pivot_df.reset_index(), id_vars=["Date"])

# Apply
df["Sales"] = df["Sales"].apply(lambda x: x + 10)

print(pivot_df)
print(melted)
print(df)