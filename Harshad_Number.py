n=int(input())
for i in range(0,n):
    a=int(input())
    t=a
    s=0
    while a>0:
        r=a%10
        s=s+r
        a=a//10
    if t%s==0:
        print("YES",end="
")
    else:
        print("NO",end="
")