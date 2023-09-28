a=int(input())
l=list(map(int,input().split()))
k=int(input())
v=[]
for i in range(a):
    if l[i]==k:
        v.append(i)
if len(v)==0:
    print("-1")
else:
    print(*v)