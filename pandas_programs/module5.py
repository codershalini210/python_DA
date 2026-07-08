import pandas as pd

df = pd.DataFrame({
    "name": ["Amit", "Neha", "Raj","Aman","Ronit"],
    "marks": [80, 90, 85,55,24],
    "age":[12,15,17,14,16]
}) #, index=["a", "b", "c"])
# df.index = ["a","b","c","d","e"]
# print(df.loc["b":"d"])
# print(df[["name" , "age"]]) #figure it out 

print(df["age"]>15)
print(df[df["age"]>15])
print(df[(df["age"]>15) & (df["marks"]>34)])

# print(True & True)
# print(df.iloc[1:3])