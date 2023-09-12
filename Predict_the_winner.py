a=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(a):
    if i%2==0 or i==0:
        s=s+l[i]
    else:
        c=c+l[i]
if s>c:
    t=s-c
else:
    t=c-s
if t%4==0:
    print("X")
else:
    print("Y")