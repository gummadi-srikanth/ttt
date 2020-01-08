s=input()
d={"UPPER":0,"LOWER":0}
for i in s:
    if i.isupper():
        d["UPPER"]+=1
    if i.islower():
        d["LOWER"]+=1
print(d)