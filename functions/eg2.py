# def calculate(a,b):
#     return a+b,a-b,a*b,a/b
# s,d,m,dv = calculate(10,2)
# print(f"sum is {s} , difference is {d} , multiplicaiton : {m},division {dv}")

# sq = lambda x :x *x
# print(sq(4))

numbers = [1, 2, 3, 4]

# result = list(map(lambda x: x * 2, numbers))
result = list(map(lambda x:x * x,numbers))
print(result)

cubes = list(map( lambda x :x*x*x  , list(range(1,5))))
print(cubes)
