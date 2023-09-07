a=int(input())
ls=list(map(int,input().split()))
for i in range(a):
    c=0
    for j in range(a):
        if ls[j]==ls[i]:
            c+=1
    if c>1:
        print(ls[i])
        break