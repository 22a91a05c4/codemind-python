a=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[j]==l[i]:
            c+=1
    if l[i]==c:
        k.append(l[i])
g=[]
for i in k:
    if i not in g:
        g.append(i)
f=len(g)
if f==0:
    print("-1")
else:
    print(*g)