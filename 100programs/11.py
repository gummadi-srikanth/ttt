value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if intp%5==0:
        value.append(p)
print(value)