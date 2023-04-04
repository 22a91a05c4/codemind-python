def bigg(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
m,n,o=map(int,input().split())
p=bigg(m,n,o)
print(p)