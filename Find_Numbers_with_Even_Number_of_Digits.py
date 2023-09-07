a=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(len(ls)):
    t=len(str(ls[i]))
    if t%2==0:
        c+=1
print(c)