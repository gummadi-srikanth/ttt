n1=10
n2=100
for i in range(n1,n2+1):
    if i>1:
        for num in range(2,i):
            if i%num==0:
                print("it is not prime number")
                break
        else:
            print(i)

