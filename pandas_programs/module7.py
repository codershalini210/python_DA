import pandas as pd 
df = pd.DataFrame({
    "name":["Anil","Rajat","Shreya"],
    "marks": [25,65,74]
})
# print(df)
df["bonus"]=5
df["midsem"]=[15,18,17]
df["marks"]=df["marks"]+df["bonus"]
print(df)
df["marks"]=df["marks"].map(lambda x: x + 10)
df["result"]=df["marks"].apply(lambda x: "Pass" if x > 40 else "Fail")
print(df)
df.replace({"Anil": "Anil sharma", "Rajat":"Rajat verma"},inplace=True)
print(df)

# df={"name":[a,b,c,d],
#     "marks":[[55,46,64],[52,63,45]....]}
# df->  result -> pass/fail -> show ist or 2nd division if pass,
#df -> print topper name 
#df -> print name of subject with max pass students
#df -> print name of subject with min pass students
#df -> print name of subject with max marks 
#df -> print name of subject with min marks