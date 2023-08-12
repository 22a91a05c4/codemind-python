n=int(input())
a=list(map(int,input().split()))
ls=sorted(a)
b=n//2
for i in range(0,n):
    print(ls[b])
    break