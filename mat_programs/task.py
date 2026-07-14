import pandas as pd
import matplotlib.pyplot as plt

# Creating DataFrame
df = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Sales": [45000,52000,48000,61000,68000,72000,75000,71000,69000,73000,78000,85000],
    "Profit": [5000,6500,5500,8200,9000,9800,10500,10200,9700,10800,11500,12500],
    "Orders": [120,140,135,160,175,185,195,190,182,200,210,225],
    "Expenses": [40000,45500,42500,52800,59000,62200,64500,60800,59300,62200,66500,72500],
    "Customers": [95,102,100,115,122,130,138,135,132,142,150,160],
    "Returns": [8,10,9,7,6,5,8,9,7,6,5,4]
})

print("\n========= SELECT DATA =========")
print("1. Monthly Sales")
print("2. Monthly Profit")
print("3. Monthly Orders")
print("4. Monthly Expenses")
print("5. Monthly Customers")
print("6. Monthly Returns")
print("7. Sales vs Profit (Scatter Plot)")
print("8. Exit")

choice = int(input("Enter your choice: "))

if choice == 8:
    print("Program Closed")

elif choice == 7:
    plt.scatter(df["Sales"], df["Profit"])
    plt.title("Sales vs Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.grid(True)
    plt.show()

else:

    if choice == 1:
        column = "Sales"
        title = "Monthly Sales"

    elif choice == 2:
        column = "Profit"
        title = "Monthly Profit"

    elif choice == 3:
        column = "Orders"
        title = "Monthly Orders"

    elif choice == 4:
        column = "Expenses"
        title = "Monthly Expenses"

    elif choice == 5:
        column = "Customers"
        title = "Monthly Customers"

    elif choice == 6:
        column = "Returns"
        title = "Monthly Returns"

    else:
        print("Invalid Choice")
        exit()

    print("\n------ SELECT GRAPH ------")
    print("1. Line Plot")
    print("2. Bar Chart")
    print("3. Histogram")
    print("4. Pie Chart")

    graph = int(input("Enter Graph Choice: "))

    if graph == 1:
        plt.plot(df["Month"], df[column], marker="o")
        plt.title(title)
        plt.xlabel("Month")
        plt.ylabel(column)
        plt.grid(True)

    elif graph == 2:
        plt.bar(df["Month"], df[column])
        plt.title(title)
        plt.xlabel("Month")
        plt.ylabel(column)

    elif graph == 3:
        plt.hist(df[column], bins=5)
        plt.title(column + " Distribution")
        plt.xlabel(column)
        plt.ylabel("Frequency")

    elif graph == 4:
        plt.pie(df[column], labels=df["Month"], autopct="%1.1f%%")
        plt.title(title)

    else:
        print("Invalid Graph Choice")
        exit()

    plt.show()