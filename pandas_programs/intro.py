import pandas as pd
numbers =[12,32,1,23,13]
print(numbers)
n = pd.Series(numbers)
print(n)
student ={
    "name":["Maria","John","Ron","Sam"],
    "marks":[98,78,86,59]
}
s = pd.DataFrame(student)
print(s)
# ......................
students ={
    "name":["Maria","John","Ron","Sam"],
    "marks":[[43,23,53,22],[78,64,34,54],[42,55,643,23],[34,65,34,65]]
}
s = pd.DataFrame(students)
print(s["name"])