import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Raj"],
    "Marks": [80, 95, 85]
})
print(df)
df.sort_values(by="Marks",ascending=False,inplace=True)
print(df)
df.sort_index(inplace=True)
print(df)