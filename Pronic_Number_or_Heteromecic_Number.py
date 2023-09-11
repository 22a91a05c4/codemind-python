a=int(input())
c=0
for i in range(a):
    if i*(i+1)==a:
        c=c+1
if c>0:
    print("YES")
else:
    print("NO")