# students = ["John","Ron","Bob","Maria"]
# print(students)
# print(stu1dents[0])
# print(students[2])

# # l = len(students)
# # students[l-1]
# print(students[-1])

# l = len(students)
# print("Total no of students ",l)
# -----------------------------------
# sals = [25632,65231,85263,12345,85412,36521]
# maximum = max(sals)
# total = sum(sals)
# minimum = min(sals)
# avg = sum(sals)/len(sals)
# print("maximum ",maximum)
# print("avg ",avg)
# print("total ",total)   
# print("minimum",minimum)
# sals = [25632,65231,85263,12345,85412,3652]
# print(sals[:3])
# print(sals[2:4])
# print(sals[2:])
# print(sals[5:3:-1])
# print(sals[0:5:2])
# print(sals[::-1])
# sals[0] = 10000
# sals[-1]=11111
# print(sals)
# sals.append(22222)
# print(sals)
# # sals.insert()
# sals.extend([111111,255555])
# print(sals)
# sals.insert(2,50000)
# print(sals)
# students = ["John","Ron","Bob","Maria"]
# sname = input("Enter STudent name ")
# if(sname in students):
#     print(sname," is present")
# else:
#     print(sname," is absent")
# students = []
# students.append(input("Enter student name"))
# students.append(input("Enter student name"))
# students.append(input("Enter student name"))
# students.append(input("Enter student name"))
# students.append(input("Enter student name"))

# students.extend([(input("Enter student name")),(input("Enter student name")),(input("Enter student name")),(input("Enter student name")),(input("Enter student name"))])
# print(students[::-1])
# add 5 students in list 
# using input , and show list in reverse order

# students = ["John","Ron","Bob","Maria"]
# numbers = [12,43,245,23]
# print(numbers)
# numbers.reverse()
# print(numbers)

# numbers.sort()
# print(numbers)

# numbers.sort()
# numbers.reverse()
# print(numbers)

# numbers = [12,43,245,23]
# t =numbers[0]
# numbers[0] = numbers[-1]
# # numbers[0] =len(numbers)-1
# numbers[-1] = t
# print(numbers)

# Given a list of 5 numbers, find the maximum 
# value using conditional statements (no max()).
# l = [12000,2500,35000,120,500]
# m = l[0]
# if(m>l[1] and m>l[2] and m>l[3] and m>l[4]):
#     print(m)
# else:
#     m=l[1]
#     if(m>l[2] and m>l[3] and m>l[4]):
#         print(m)
#     else:
#         m=l[2]
#         if(m>l[3] and m>l[4]):
#             print(m)
#         else:
#             m = l[3]
#             if(m>l[4]):
#                 print(m)
#             else:
#                 print(l[4])
# ---------------------------
# print(max(l))
# if(m<l[1]):
#     m=l[1]
#     if(m<l[2]):

#         m=l[2]
#         if(m<l[3]):
#             m = l[3]
#             if(m<l[4]):
#                 m = l[4]
# else:
#     if(m<l[2]):
#         m=l[2]
#         if(m<l[3]):
#             m = l[3]
#             if(m<l[4]):
#                 m = l[4]
# Split a list into two halves using slicing.
# l = [12,23,43,53,64,403]
# l = [12,23,43,53,64,43,89,45,85]
# length = len(l)
# x=(int(length/2))
# print(x)
# print("first list",l[0:x])
# print("second list",l[x:])
# -------------------------
# students = ["Raman","Aman","Tapan","Maulik"]
# marks = [ [32,43,23],
#          [43,54,35],
#          [53,56,23],
#          [78,65,84]]
# print("marks of raman are ", marks[0], sum(marks[0])/len(marks[0]),)
students = {"raman":45,"Aman":52,"kaushik":32}
print(students)
print(students["raman"])
# print(students[0]) throws error