import numpy as np

# sales = np.array([
#     [10000,12000,15000],
#     [11000,13000,16000],
#     [12000,14000,17000]
# ])
# print(np.sum(sales)) 
# print(np.sum(sales,axis=0))
# print(np.sum(sales,axis=1))
# print(np.sum(sales[0]))
# print(np.sum(sales[:,0]))

# print(sales)
# print("avg of axis 0 ",np.average(sales,axis=0))
# print("avg of axis 1",np.average(sales,axis=1))
# print("mean of axis 0 ",np.mean(sales,axis=0))
# print("mean of axis 1",np.mean(sales,axis=1))
# print("median of axis 0 ",np.median(sales,axis=0))
# print("median of axis 1",np.median(sales,axis=1))
# marks = np.array([
#     [50,55,60],
#     [35,40,50],
#     [65,75,85]
# ])
# print("total marks of student", np.sum(marks,axis=1))
# print("average marks of student", np.average(marks,axis=1))
# print("average marks per subject", np.average(marks,axis=0))
# •	Create a  2d array that contains every row as student, and columns as marks of student s,
# •	[]
# •	Generate marks using random , marks should be between 25,100
# marks = np.array([np.random.randint(25,101,5),
#                   np.random.randint(25,101,5)
#                   ,
#                   np.random.randint(25,101,5),
#                   np.random.randint(25,101,5),
#                   np.random.randint(25,101,5)])
marks = np.random.randint(25,101,(5,5))
print(marks)
# •	Give  topper marks
print("student marks ", np.sum(marks,axis=1))
print("Topper marks ", np.max(np.sum(marks,axis=1)))

# # •	Give avg marks 
# print("average marks ",np.average(marks))
# # •	Give avg marks per student
# print("average marks per student ",np.average(marks,axis=1))
# # •	Give avg marks per subject
# print("average marks per subject ",np.average(marks,axis=0))

# # •	Find max marks per student
# print("max marks per student ",np.max(marks,axis=1))

# # •	Give max marks per subject 
# print("max marks per subject ",np.max(marks,axis=0))
# # •	Find min marks per student
# # •	Give min marks per subject 

