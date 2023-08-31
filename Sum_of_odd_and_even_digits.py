a=int(input())
ls=list(map(int,input().split()))
o=0
e=0
for i in range(a):
    if i%2==0:
        e=e+ls[i]
    else:
        o=o+ls[i]
d=e-o
if d==0:
    print("YES")
else:
    print("NO")