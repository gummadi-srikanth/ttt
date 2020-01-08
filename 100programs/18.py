import re
value=[]
items=[x for x in input().split(",")]
for a in items:
    if len(a)<6 or len(a)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",a):
        continue
    elif not re.search("[A-Z]",a):
        continue
    elif not re.search("[1-9]",a):
        continue
    elif not re.search("[@#$]",a):
        continue
    elif not re.search("\s",a):
        continue
    else:
        pass
    value.append(a)
print(value)
