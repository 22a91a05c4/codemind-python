a=int(input())
ls=list(map(int,input().split()))
k=int(input())
d=[]
for i in range(a):
    if k==ls[i]:
        d.append(i)
if (len(d))>0:
    print(min(d),max(d))
else:
    print("-1 -1")