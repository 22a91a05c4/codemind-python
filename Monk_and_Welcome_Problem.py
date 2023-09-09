a=int(input())
ls=list(map(int,input().split()))
it=list(map(int,input().split()))
for i in range(a):
    d=ls[i]+it[i]
    print(d,end=" ")