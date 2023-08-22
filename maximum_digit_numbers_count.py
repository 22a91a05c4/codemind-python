a=int(input())
ls=list(map(str,input().split()))
k=[]
p=[]
for i in range(0,a):
    m=len(ls[i])
    k.append(m)
b=max(k)
for i in range(len(k)):
    if b==k[i]:
        p.append(ls[i])
print(*p)