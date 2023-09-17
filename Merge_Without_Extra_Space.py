a=int(input())
for i in range(a):
    c,d=map(int,input().split())
    g=list(map(int,input().split()))
    h=list(map(int,input().split()))
    b=[]
    for j in range(c):
        b.append(g[j])
    for k in range(d):
        b.append(h[k])
    f=sorted(b)
    print(*f)