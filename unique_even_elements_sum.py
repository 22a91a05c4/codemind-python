n=int(input())
ls=list(map(int,input().split()))
k=[]
c=0
for i in range(0,n):
    if ls[i] not in k:
        k.append(ls[i])
for i in range(0,len(k)):
    if k[i]%2==0:
        c+=k[i]
print(c)