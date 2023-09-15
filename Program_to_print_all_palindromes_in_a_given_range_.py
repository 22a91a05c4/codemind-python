a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    t=i
    s=0
    while(i):
        r=i%10
        s=s*10+r
        i=i//10
    if s==t:
        l.append(t)
print(*l)