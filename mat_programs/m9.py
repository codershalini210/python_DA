import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40,30,20,10]

ax1.plot(x, y1, color="blue")
ax1.set_ylabel("Sales", color="blue")

ax2 = ax1.twinx()
ax2.plot(x, y2, color="red")
ax2.set_ylabel("Revenue", color="red")

plt.title("Twin Axes Example")
plt.savefig("plot.png", dpi=300)
plt.show()


# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y1 = [10, 20, 30, 40]
# y2 = [40, 30, 20, 10]

# # f,a=plt.subplots(2,2)
# # a[0][0].plot(x,y1)
# # # f.set
# # a[1][0].plot(x,y2)
# # plt.show()

# # plt.figure(figsize=(8,8))
# plt.subplot(1, 2, 1)
# plt.plot(x, y1,label="first")
# plt.xlabel("x -axis")
# plt.ylabel("data1")
# plt.title("Plot 1")
# plt.legend()
# plt.subplot(1, 2, 2)
# plt.plot(x, y2,label="second")

# plt.xlabel("x -axis")
# plt.ylabel("data2")
# plt.title("Plot 2")
# plt.tight_layout()
# plt.legend()
# plt.grid(True)
# plt.show()
# # plt.subplot(2, 2, 1)
# # plt.plot(x, [10, 20, 30, 40])
# # plt.title("Plot 1")

# # plt.subplot(2, 2, 2)
# # plt.plot(x, [40, 30, 20, 10])
# # plt.title("Plot 2")

# # plt.subplot(2, 2, 3)
# # plt.bar(x, [5, 10, 15, 20])
# # plt.title("Plot 3")

# # plt.subplot(2, 2, 4)

# # plt.scatter(x, [2, 4, 6, 8])
# # plt.title("Plot 4")

# # plt.tight_layout()
# # plt.show()

