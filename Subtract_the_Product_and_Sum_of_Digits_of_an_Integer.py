n=int(input())
s=0
f=1
while n:
    r=n%10
    s=s+r
    f=f*r
    n=n//10
if s>f:
    c=s-f
else:
    c=f-s
print(c)