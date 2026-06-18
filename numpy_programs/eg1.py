import numpy as np

rns = np.random.randint(10,25,5)
flag = True
count = 0
while(flag):  
          
    n = int(input("Guess any no between 10-25"))
    if(n in rns):
        print("you won ")
        flag=False
    else:
        print("you loss")
        count=count+1
        if(count>3):
            print("game over")
            flag=False
print(rns)