a=int(input())
s=0
if a>0:
    while(a):
        r=a%10
        s=s*10+r
        a=a//10
    print(s)
elif a<0:
    b=-1*(a)
    while(b):
        r=b%10
        s=s*10+r
        b=b//10
    print(-s)
else:
    print("0")