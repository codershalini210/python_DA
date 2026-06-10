text = "apple banana apple mango orange banana apple mango orange"
words =text.split()
print(words)
f = {}
for w in words:
    if (w in f.keys()):
        f[w]= f[w]+1
    else:
        f[w] =1
print(f)
print(f["orange"])
print(f.get("orange"))

print(f.get("kiwi")) #return none when key is not present   
# print(f["kiwi"])  #throws error when key is not present


f.pop("apple")      # Removes specific key
print(f)
del f["mango"]     # Deletes key
print(f)
f.clear()         # Empties dictionary 
print(f)

# squares = {x: x*x for x in range(5)}
# print(squares)
std = dict(classname ="First", section ="a")
print(std)
