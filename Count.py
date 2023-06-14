n=int(input())
c=0
s=0
ls=list(map(int,input().split()))
for i in range(len(ls)):
    if ls[i]%2==0:
        c+=1
    else:
        s+=1
print(c,s)