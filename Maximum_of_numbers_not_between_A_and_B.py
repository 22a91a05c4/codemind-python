a=int(input())
ls=list(map(int,input().split()))
k=[]
c=0
m,n=map(int,input().split())
for i in range(0,a):
    if ls[i]<m or ls[i]>n:
        k.append(ls[i])
        c+=1
if c>=1:
    print(max(k))
else:
    print("-1")