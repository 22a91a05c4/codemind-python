a=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(a):
    if ls[i]==0 or ls[i]==1:
        c+=1
if c==a:
    print("True")
else:
    print("False")