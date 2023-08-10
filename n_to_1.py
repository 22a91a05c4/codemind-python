a=int(input())
ls=[]
for i in range(1,a+1):
    ls.append(i)
b=reversed(ls)
print(*b)