a=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    c=0
    for j in range(1,i+1):
        if (j*j)==i:
            c+=1
    if c>0:
        s=s+i
print(s)