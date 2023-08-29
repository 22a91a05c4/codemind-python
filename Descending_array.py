a=int(input())
ls=list(map(int,input().split()))
d=sorted(ls)
c=0
k=d[::-1]
for i in range(a):
    if ls[i]==k[i]:
        c+=1
if c==a:
    print("yes")
else:
    print("no")