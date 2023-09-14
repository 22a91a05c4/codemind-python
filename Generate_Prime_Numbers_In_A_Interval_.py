def pri(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return n
    else:
        return 0
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    g=pri(i)
    if g==i:
        l.append(i)
for i in range(len(l)):
    print(l[i],end="
")