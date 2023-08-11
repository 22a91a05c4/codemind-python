a=int(input())
ls=list(map(int,input().split()))
k=[]
for i in range(0,a):
    if ls[i] not in k:
        k.append(ls[i])
print(*k)