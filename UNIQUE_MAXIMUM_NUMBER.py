a=int(input())
ls=list(map(int,input().split()))
t=[]
for i in range(a):
    c=0
    for j in range(a):
        if ls[j]==ls[i]:
            c+=1
    if c==1:
        t.append(ls[i])
if (len(t))==0:
    print("-1")
else:
    print(max(t))