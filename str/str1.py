# text = "  python learning . hello world from python   "

# # print(text.upper())      
# # print(text.lower())      
# # print(text.title())      
# # print(text.capitalize()) 
# print(text)
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# text= text.replace("python","js",1)
# print(text)

# text = "a"

# print(text.isalpha())   
# print(text.isdigit())   
# print(text.isalnum()) 
# # Escape Characters
# print("Hello\nWorld")   
# print("Hello\tWorld")   
# print("He said \"Hi\"") 

username ="mohit"
print(username)
# username="Rohit"
# username[0]="R"
print(username)

sentence = "  python is easy to learn  "

clean = sentence.strip().title()

print(clean)
n = clean.split()
print(n)

cityname ="Ahmedabad"
print(cityname[::-1])

username = input("Enter your name ")
count=0
for v in username.lower():
    if(v in "aeiou"):
        count+=1
msg = f"your name has {count} no of vowels"
print(msg)