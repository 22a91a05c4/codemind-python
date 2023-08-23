n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(n):
    if ls[i]<n:
        c+=1
for i in range(n):
    if c==n:
        print("YES")
        break
    else:
        print("NO")
        break