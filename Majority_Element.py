a=int(input())
ls=list(map(int,input().split()))
l=[]
for i in range(a):
    c=0
    t=ls[i]
    for j in range(a):
        if t==ls[j]:
            c+=1
    l.append(c)
d=max(l)
for i in range(a):
    if l[i]==d:
        print(ls[i])
        break