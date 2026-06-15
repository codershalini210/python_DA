file = open("data.txt","r")
# data = file.read()   read complete file
# print(data)

# line = file.readline()   read first line
# print(line)

lines = file.readlines()
print(lines[0:3])
file.close()