import numpy as np 
sales = np.array([1000, 2000, 3000, 4000, 5000])
# print("first element is ", sales[0])
# print("Last element is ",sales[-1])

data = np.array([
    [101,1000],
    [102,2000],
    [103,3000]
])

# print(data[0,0])
# print(data[1,1])
# print(data[2,0])
# print(data)
# data[0,0]=111
# print(data)
# print(data[0])
# print(data[:,0])

emps =np.array([
    [101,36,65,45,85,64],
    [102,38,25,29,75,34],
    [103,76,65,45,85,64],
    [104,33,45,47,55,44],
    [105,46,65,49,75,60],
])
# print(sales)
# print(sales[1:3])
# print(sales[::-1])
# print(sales[0:5:2])
# print(emps[:,1:3])
# print(emps)
# print(emps[0:3:2,0:5:2])
print(sales>2000)
print(sales[sales>2000])
result =sales[sales>2000]
print(result)