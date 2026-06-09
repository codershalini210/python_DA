# l = ["a","b","c","d"] 
# for i in l :
#     print(i)
# -------------------
# salaries = [45000,34000,65000,56000]
# s = 0 
# m = salaries[0]
# mn = salaries[0]
# for sal in salaries:
#     s= s+sal
#     if(m<sal):
#         m = sal
#     if(mn>sal):
#         mn=sal    
# print("Total salary " ,s) 
# print("Max salary ", m)
# print("Min salary ", mn)
# --------------------

# l = list(range(5))
# print(l)
# print("********************")

# l = list(range(2,5))
# print(l)


# l = list(range(1,5,2))
# print(l)

# lst = list(range(1,11))
# for  n in lst:
#     print(n)
   
# for m in range(1,11):
#     # print(m)
#     if(m%2==0):
#         print(m)

# for n in range(10,0,-1):
#     print(n)
    # Count how many numbers are greater than 20 in [5, 25, 15, 30, 10].

# n = int(input("Enter any no "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")

n = int(input("Enter any no "))
fact = 1 
# for i in range(1,n+1):
for i in range(n,0,-1):
    fact = fact * i 

# 4!   = 4*3*2*1
# 5!= 5*4*3*2*1
# fact
print(f" factorail of {n} is {fact}")