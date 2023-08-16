n=int(input())
ls=list(map(int,input().split()))
r=[]
s=0
for i in range(0,n):
    if ls[i] not in r:
        r.append(ls[i])
        s=s+ls[i]
print(s)