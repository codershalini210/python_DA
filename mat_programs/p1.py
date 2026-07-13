import numpy as np 
import matplotlib.pyplot as plt
# x=[1,2,3,4]
# x=["jan","feb","mar","Apr"]
# y=[10,5,30,2]
# plt.plot(x,y)
# plt.show()

# x = [1, 2, 3, 4]
# y1 = [10, 20, 15, 25]
# y2 = [50, 5, 10, 100]
# plt.plot(x,y1,label="product1")
# plt.plot(x,y2,label="product2")
# plt.title("Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("sales")
# plt.legend()
# plt.grid(True)
# plt.show()


months = ["jan","feb","mar","apr","may"]
sales_A = [100, 120, 90, 150, 200]
sales_B = [90, 110, 90, 110, 100]
x = np.arange(len(months))

plt.bar(x-0.2,sales_A,width=0.3,label="A")
plt.bar(x+0.2,sales_B,width=0.3,label="B")
# plt.bar(0.8,months,sales_A,color="red",label="A")
# plt.bar(1.2,months, sales_B,color="blue",label="B")
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(x,months)
plt.grid(True)
plt.show()
