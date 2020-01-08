s=input()
d={"DIGITS":0,"LETTERS":0}
for i in s:
    if i.isdigit():
        d["DIGITS"]+=1
    if i.isalpha():
        d["LETTERS"]+=1
print(d)