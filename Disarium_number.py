a=int(input())
m=len(str(a))
c=0
h=a
while a:
    while m:
        r=a%10
        t=r**m
        c=c+t
        a=a//10
        m=m-1
if c==h:
    print("True")
else:
    print("False")