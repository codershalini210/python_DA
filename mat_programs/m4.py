import matplotlib.pyplot as plt
# data = [10, 20, 20, 30, 30, 30, 40, 50, 60]
# plt.hist(data,edgecolor="red")  #,bins=3)
# plt.title("Marks ")
# plt.show()
# data =[40,30,30,20]
# labels=["a","b","c","d"]
# explode = [0.1, 0, 0,0]
# plt.pie(data,labels=labels,explode=explode)
# plt.show()



# companies = ["Company A", "Company B", "Company C", "Company D"]
# market_share = [35, 25, 20, 20]
# explode=[0.01,0.01,0.01,0.01]
# colors =["red","green","blue","yellow"]
# plt.pie(market_share, labels=companies, autopct="%1.2f%%",colors=colors,
#         shadow=True,explode=explode,radius=1.2)# ,rotatelabels=True)

# plt.title("Market Share Analysis")
# plt.show()

x =[1,2,3,4,5]
# y =[ 10,20,30,40,50]
y=[10,8,5,3,1]
plt.scatter(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()