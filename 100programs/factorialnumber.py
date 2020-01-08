# num=7
# factorial=1
# if num<0:
#     print("not applicable for negative numbers")
# elif num==0:
#     print("it is zero")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(factorial)

#factorial number by using recursion
def factorial(n):
    if n== 1:
        return n
    else:
        return n*factorial(n-1)
num=7
if num<0:
    print("soryy it is not taken")
elif num==0:
    print("factorial of 0 is 1")
else:
    print(factorial(num))