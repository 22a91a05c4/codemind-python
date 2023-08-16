n=int(input())
ls=list(map(int,input().split()))
k=[]
c=0
for i in range(0,n):
    if ls[i] not in k:
        k.append(ls[i])
for j in range(0,len(k)):
    if k[j]%2!=0:
        c+=1
print(c)