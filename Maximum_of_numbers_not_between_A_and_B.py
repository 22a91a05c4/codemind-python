a=int(input())
ls=list(map(int,input().split()))
k=[]
c=0
n,m=map(int,input().split())
for i in range(a):
    if(ls[i]<n or ls[i]>m):
        k.append(ls[i])
        c+=1
if c>0:
    print(max(k))
else:
    print("-1")