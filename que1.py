students={}
for i in range(5):
    name = input("Enter student name ")
    marks=[]
    for j in range(5):
        marks.append(int(input("Enter marks")))
    students[name]=marks
passdict={}
faildict={}
for key,value in students.items():
    print(key,value)
    if(min(value)>34):
        passdict[key] = sum(value)
    else:
        faildict[key] = sum(value)
print("no of pass students ", len(passdict))
print("no of fail students ",len(faildict))
print(" pass students ", passdict)
print("fail students ",faildict)
# print("Topper ",max(passdict))
toppername = ""
maxmarks = 0
for k,v in passdict.items():
    if(maxmarks<int(v)):
        toppername=k
        maxmarks = v


print("Topper ",toppername," marks ",maxmarks)
