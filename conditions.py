# 14 Take a character input.
# If it is lowercase letter, then check if it is vowel or consonant
# using nested if (no logical operators).
ch = input("Enter any character")
if(ch.islower()):
    # check vowel or consonent
    if(ch=="a"):
        print(ch ,"is Vowel")
    elif(ch=="e"):
        print(ch ,"is Vowel")
    elif(ch=="i"):
        print(ch ,"is Vowel")
    elif(ch=="o"):
        print(ch ,"is Vowel")
    elif(ch=="u"):
        print(ch ,"is Vowel")
    else:
        print(ch ," is consonent")
else:
    print(ch," is not in lower case")

# username = input("Enter your name")
# age = int(input("Enter your age"))
# if(age>17):
#     if(age<121):
#         print(f"{username} you are eligible to vote")
#     else:
#         print("Invalid age")
# else:
#     if(age>0):
#         print(f"{username} you are NOT eligible to vote")
#     else:
#         print("Invalid age")

# # 1. take studentname and marks as input and show its pass or fail

# #2. take name and age as input and show its senior citizen or not

# #3. take name and salary , if salary is greater than 50000 show
# # 10% of salary as bonus
# #or if salary is less than 50000 show 20% of salary as bonus

# # 4 take no of units -> caluate bill @5rs if units are less than 50 else @7 






# # print(f"{username} you are eligible to vote")
# # print(f"{username} you are not eligible to vote")
