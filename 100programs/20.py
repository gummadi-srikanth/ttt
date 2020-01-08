def putnumbers(n):
    i=0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j
for i in reversed(int(100)):
    print(i)
