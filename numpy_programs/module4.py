import numpy as np 
marks =np.array([
    ["John",65],
    ["Ron",25],
    ["Maria",68],
    ["Sam",34]
])
print((marks[:,1]).astype(int))
print(marks[(marks[:,1]).astype(int)>34])