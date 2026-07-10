import pandas as pd 
df1 = pd.DataFrame({
    "ID": [1, 1, 2],
    "Name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Marks": [80, 90]
})

print(pd.merge(df1, df2, on="ID"))
# df1=pd.DataFrame({
#     "id":[1,2,3,4],
#     "name":["a","b","c","d"]
# })
# df2=pd.DataFrame({
#     "id":[1,2,3,5],
#     "marks":[80,45,63,66]
# })
# # print(pd.merge(df1,df2,how="outer",on="id"))
# # print(pd.merge(df1,df2,how="cross"))
# # print(pd.concat([df1,df2]))   #row wise
# # print(pd.concat([df1,df2],axis=1))
# # print(pd.concat([df1, df2], axis=1))
# df1=df1.set_index("id")
# df2=df2.set_index("id")
# df_joined=(df2.join(df1))
# print(df_joined)