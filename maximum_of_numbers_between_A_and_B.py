a=int(input())
ls=list(map(int,input().split()))
n,m=map(int,input().split())
k=[]
c=0
for i in range(0,a):
    if ls[i]>=n and ls[i]<=m:
        k.append(ls[i])
        c+=1
if c>0:
    print(max(k))
else:
    print("-1")
