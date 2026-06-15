import os
if os.path.exists("a.txt"):
    with open("a.txt","r") as file:
     print(file.read())
else:
    print("file not found")
# file = open("demo.txt","w")
# file = open("demo.txt","a")
# file.write("\nhello world ")
# file.close()
# print("file written")
# with open("demo.txt","a") as file:
#     flag = "y"
#     while(flag=="y"):            
#             name = input("enter student name ")
#             marks = int(input("Enter marks"))
#             msg = f"name : {name} marks :{marks} \n"
#             file.write(msg)
#             print("dataadded")
#             flag = input("press y to continue an  \n any other key to exit ")