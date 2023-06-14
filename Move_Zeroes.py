n=int(input())
ls=list(map(int,input().split()))
k=[]
for i in range(len(ls)):
    if ls[i]!=0:
        print(ls[i],end=" ")
for j in range(len(ls)):
    if ls[j]==0:
        k.append(ls[j])
for l in range(len(k)):
    print(k[l],end=" ")