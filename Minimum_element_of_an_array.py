a=int(input())
ls=list(map(int,input().split()))
for i in ls:
    if i>i+1:
        m=i+1
    else:
        m=i
print(m)