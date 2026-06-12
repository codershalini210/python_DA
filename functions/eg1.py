# def hello():
#     print("hello world")
#     print("this message is from hello function ")
    
# hello()
# hello()

# def greet(username):
#     print("welcome ", username)
# greet("Aman")
# greet("Ronit")

# def sum1(a,b):
#     print(f"{a} + {b} ={a+b}")
# sum1(10,20)

# def user(name,age):
#     if(age>17):
#         print(f"{name } you are eligible to vote")
#     else:
#         print(f"{name } you are not eligible to vote")

# user("Ram",45)
# user(age=12,name="Maria")

# def nationality(username,nation="India"):
#     print(f"{username } you select {nation}")
    
# nationality("John","USA")
# nationality("Aman")

def sumn(*args):
    s = 0 
    for n in args:
        s = s+n
        
    return s
    
print(sumn(12,43,32,5,3,5,3))
print(sumn(12,32,42,5))