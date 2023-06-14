n=int(input())
ls=list(map(int,input().split()))
for i in range(len(ls)):
    if ls[i]==0:
        print(ls[i],end=' ')
for j in range(len(ls)):
    if ls[j]==1:
        print(ls[j],end=' ')