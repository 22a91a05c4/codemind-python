a=int(input())
ls=list(map(int,input().split()))
h=[]
for i in range(a):
    b=ls[i]
    c=1
    for j in range(a):
        if ls[j]!=b:
            c=c*ls[j]
    h.append(c)
print(*h)