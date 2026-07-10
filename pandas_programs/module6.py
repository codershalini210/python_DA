import pandas as pd 
# df = pd.read_excel("Basic Excel.xlsx","Sheet2")

# print(df.head())
# print(df["fullname"])
# print(df["fullname"].str.lower())
# print(df["fullname"].str.upper())
# print(df["fullname"].str.capitalize())
# print(df["fullname"].str.len())
# print(df["fullname"].str.lower())
# messages = [
#     "Good morning have a wonderful day",
#     "Please complete your assignment today",
#     "Meeting starts at ten in the morning",
#     "Happy birthday wish you great success",
#     "Thank you for your valuable support",
#     "Your order has been shipped successfully",
#     "Welcome to our Python programming course",
#     "Practice coding every day to improve",
#     "Please submit the report before Friday",
#     "Congratulations on your amazing achievement",
#     "The project deadline is approaching soon",
#     "Keep learning and never stop growing",
#     "Your payment has been received successfully",
#     "Please check your email for updates",
#     "The class will begin in five minutes",
#     "Have a safe and pleasant journey",
#     "Remember to save your work frequently",
#     "Your account has been updated successfully",
#     "Please restart the application and try again",
#     "New features have been added this week",
#     "Thank you for choosing our services",
#     "Your registration is now complete",
#     "Please enter a valid email address",
#     "Learning Python becomes easier with practice",
#     "Always write clean and readable code",
#     "Do not forget to backup your files",
#     "Your password has been changed successfully",
#     "Welcome back we missed you",
#     "The server is running without errors",
#     "Please contact support for assistance",
#     "Enjoy your learning journey with us",
#     "Your booking has been confirmed successfully",
#     "This document contains important information",
#     "Keep your software updated regularly",
#     "Your session has expired please login again",
#     "The download completed without any issues",
#     "Please verify your mobile number first",
#     "Today is a great day to learn",
#     "Coding helps improve logical thinking skills",
#     "Success comes from consistent hard work",
#     "Never give up on your dreams",
#     "Stay positive and keep moving forward",
#     "Every challenge is an opportunity to learn",
#     "Small steps lead to big achievements",
#     "Teamwork makes every project more successful",
#     "Please review the document carefully",
#     "The backup was completed successfully",
#     "Your feedback helps us improve",
#     "Thank you and have a nice day",
#     "See you in the next session"
# ]
df = pd.DataFrame({
    "id":[1,2,3,4,5,6],
    "msgs":["Good morning have a wonderful day",
    "Please complete your assignment today",
    "Meeting starts at ten in the morning",
    "Happy birthday wish you great success",
    "Thank you for your valuable support",
    "Your order has been shipped successfully"]

})
# print(df.info())
# print(df[df["msgs"].str.contains("in")])
# print(df[df["msgs"].str.find("success")!= -1])

# print(df["msgs"].str.replace("your","our"))

# G__d m_rn__ng 
# --------------------------------
# print(df.isnull())
# print(df["sub1"].isnull())
# df["sub1"]=df["sub1"].fillna(0)
# df["sub2"]=df["sub2"].fillna(0)
# df["sub3"]=df["sub3"].fillna(0)
# df=df.replace("Abs",None)
# df[["sub1","sub2","sub3"]]=df[["sub1","sub2","sub3"]].fillna(0)
# # print(df[["sub1","sub2","sub3"]])    #.isnull())
# df[["sub1","sub2","sub3"]]=df[["sub1","sub2","sub3"]].astype(int)

# print(df[["sub1","sub2","sub3"]].dtypes)

# for ch in "AEIOUaeiou":
#     df["msgs"] =df["msgs"].str.replace(ch,"_")
# print(df["msgs"])
# df["msgs"] =df["msgs"].str.replace(("a","e"),"_")