import math
n=int(input())
k=[]
ls=list(map(int,input().split()))
for i in range(len(ls)):
    s=ls[i]**2
    k.append(s)
d=sorted(k)
for j in range(len(d)):
    print(d[j],end=" ")