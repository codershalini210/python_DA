import numpy as np

marks = np.array([34,54,65,76,45,77])
print(marks)

rooms = np.array([
    [12,14],
    [18,15],
    [10,10]
])
print(rooms)
print("dimensions of marks ", marks.ndim)
print("dimensions of rooms",rooms.ndim)

print("shape of marks ", marks.shape)
print("shape of rooms",rooms.shape)
print("datatype of marks ",marks.dtype)
names = np.array(["Ron","John capner","Maria raghuwanshi"])
print("data type of names ", names.dtype)

zrs = np.zeros((5,2))
print(zrs)

ons = np.ones((4,3))
print(ons)

fvs = np.full((5,2),25)
print(fvs)

ary1 = np.arange(5)
print(ary1)
ary1 = np.arange(2,5)
print(ary1)
ary1 = np.arange(1,15,3)
print(ary1)
ary1 = np.linspace(0,10,5)
print(ary1)
ary1 = np.eye(3,4)
print(ary1)