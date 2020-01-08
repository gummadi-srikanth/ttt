def numbers(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if l1>l2:
        print(l1)
    elif l2>l1:
        print(l2)
    else:
        print(s1)
        print(s2)
print(numbers("123","12"))