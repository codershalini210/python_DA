import pandas as pd 
emps = pd.DataFrame({"emp1":[25000,32000,45200],
                     "emp2":[65222,52000,56000],
                     "emp3":[23652,40000,32000]})
print(emps.columns)
emps.index =["jan","feb","march"]
# print(emps.index)
print(emps)
print(emps["emp1"])
print(emps.loc["jan"])
# print(emps.loc(0))
# month wise sales
# emp wise sales
# emp name whose sales are highest
#emp name whose sales are lowest 
#avg sales per month
#avg sales per emp
#month with highest sales
#month with lowest sales
