def su(n):
    s=0
    while(n):
        r=n%10
        s=s+r
        n=n//10
    if len(str(s))>1:
        return su(s)
    return s
a=int(input())
if len(str(a))>1:
    g=su(a)
    print(g)
else:
    print(a)