# t1 = (11,22,33,44,55,33,44,33)
# print(t1)
# print(t1[2])
# print(t1[-1])
# print(t1[1:3])
# print(t1.count(33))
# print(t1.index(33))
# print(t1.index(33,3))
# singlet = (101,)
# print(singlet)


# t2 =  1,2,3
# print(t2)
# a,b,c = t2
# print(a,b)
# num1 = t2[0]
# num2 = t2[1]
# print(num1,num2)
# Create a tuple and convert it into a list. 
# Modify the list and convert it back to a tuple.
# tple = (12,123,542,123,43)
# lst = list(tple)
# lst[0]=1000
# tple =  tuple(lst)
# print(tple)

numbers =(324,23,4,53,6,456,1,3,14,54,3)
lsteven=[]
lstodd = []
for n in numbers :
    if(n%2==0):
        lsteven.append(n)
    else:
        lstodd.append(n)
tpleeven = tuple(lsteven)
tplodd = tuple(lstodd)
print("Main tuple ", numbers)
print("even tuple ", tpleeven)
print("odd tuple ", tplodd)