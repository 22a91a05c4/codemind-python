n=int(input())
for i in range(1,n+1):
    n,a,b,k=map(int,input().split())
    s=0
    c=0
    e=0
    s=n//a
    c=n//b
    e=n//(a*b)
    d=(s+c)-e
    if d>=k:
        print("Win")
    else:
        print("Lose")