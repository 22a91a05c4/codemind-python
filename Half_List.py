a=int(input())
ls=list(map(int,input().split()))
t=a//2
for i in range(a-1,t-1,-1):
    print(ls[i],end=" ")
for j in range(t):
    print(ls[j],end=" ")