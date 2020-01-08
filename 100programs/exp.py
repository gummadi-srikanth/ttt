d={1:(1,2,3),2:(4,5,6),3:(7,8,9)}
a=[i[0]for i in d.values()]
print(a)
b=[j[1]for j in d.values()]
print(b)
c=[k[2]for k in d.values()]
print(c)
l1=map(lambda x:x*x,a)
print(list(l1))
l2=map(lambda x:x*x,b)
print(list(l2))
l3=map(lambda x:x*x,c)
print(list(l3))