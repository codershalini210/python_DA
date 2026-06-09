# pincodes = {"Rajkot":345424,"Ahmedabad":282425,"Vapi":456654}
# print(pincodes)
# print("pincode of rahkit is ", pincodes["Rajkot"])
# for p in pincodes:
#     print(p)
#     print(pincodes[p])
# for k,v in pincodes.items():
#     print(k,"---",v)

# for v in pincodes.values():
#     print(v)

students = {"Ron":[25,35,41],"John":[35,65,45],"Maria":[65,85,75]
            ,"Sonia":[33,52,41]}
for k,v in students.items():
    # print(f"marks of {k} is {v}")
    # 35-44 3rd division
    # 45-59 2nd division
    # first division 
    #congratulation  Ron ,you  pass in 1st division 
    #sorry ,Maria you are fail
    flagPass = True
    msg = f"{k}  Pass"
    for m in v:
        if(m<35):
            flagPass=False
            break
        else:
            per = sum(v)/len(v)
            if(per>59):
                msg = f"passed in 1st div {per}"
            elif(per>44):
                msg =f"passed in 2nd div {per}"
            else:
                msg = f"Passed in 3rd division {per}"
    if(not flagPass):
        msg = f"  Fail"
    print(k," ",msg)