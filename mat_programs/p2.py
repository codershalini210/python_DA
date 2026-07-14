import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
data = pd.read_excel("../pandas_programs/Basic Excel.xlsx","Sheet2")
# print(data.head())
# xaxis = list(set(data["result"].values))

xaxis = list(data["result"].sort_values(ascending=False).unique())

sub1_pass = (data[data["sub1"]>34]["sub1"]).count()
sub1_fail = data["sub1"].count() -sub1_pass
sub1 = [sub1_pass+1,sub1_fail+1]

sub2_pass = (data[data["sub2"]>34]["sub2"]).count()
sub2_fail = data["sub2"].count() -sub2_pass
sub2 = [sub2_pass,sub2_fail]

sub3_pass = (data[data["sub3"]>34]["sub3"]).count()
sub3_fail = data["sub3"].count() -sub3_pass
sub3 = [sub3_pass,sub3_fail]
# sub4 = [4,6]
print(sub1,sub2,sub3)
plt.plot(xaxis,sub1,label="sub1",color="black")
plt.plot(xaxis,sub2,label="sub2")
plt.plot(xaxis,sub3,label="sub3")
# plt.plot(xaxis,sub4,label="sub4")
plt.legend()
plt.show()