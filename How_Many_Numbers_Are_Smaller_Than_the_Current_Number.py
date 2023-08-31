a=int(input())
ls=list(map(int,input().split()))
k=[]
for i in range(a):
    t=ls[i]
    c=0
    for j in range(a):
        if ls[j]<t:
            c+=1
    k.append(c)
print(*k)