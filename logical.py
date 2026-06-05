# and    or 
#C1    C2     and    or 
#T      T       T    T
# T     F       F    T
# F     T       F    T
# F     F       F    F 
# Take a number as input and
# check if it is greater than 10 and less than 50.
n = int(input("Enter any no "))
if(n<10  or n>50):
    print("no is not between 10 and 50")
else:  
    print("no is  between 10 and 50")
# -------------------------------
# if(n>10 and n<50):
#     print("no is betwenn 10 and 50")
# else:
#     print("no is not between 10 and 50")
# ---------------------
# if(n>10):
#     if(n<50):
#         print("no is betwenn 10 and 50")
#     else:
#         print("no is greater than 50")
# else:
#     print("no is less than 10")