import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "PHR", "IT", "Finance", "PHR"],
    "Empname":["a","b","c","d","e"],
    "Salary": [50000, 40000, 60000, 70000, 45000]
})

print(df.pivot_table(values="Salary",index="Department",aggfunc="sum"))
# print(df.groupby("Department")["Salary"].agg(["max","min","count","sum"]))
# print(df.groupby("Department")["Salary"].sum())
# print((df.groupby("Department")["Salary"].sum()))
# df1 =(df.groupby("Department")["Salary"].sum())
# print(df.dtypes)
# print("-------------------")
# print(df1.sort_values())
# print(df1.sort_index())
# print(df1.sort_values(by="Department"))
# print(df.sort_values(by="Salary"))
# print(grouped)