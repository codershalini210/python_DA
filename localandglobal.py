x=0
def num():
    # x= 20    another local variable with name x 
    global x 
    x = x+1
    print("function called ",x, " no of times")
num()
num()
num()
