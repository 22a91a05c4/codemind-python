a=int(input())
l=list(map(int,input().split()))
g=sorted(l)
k=[]
for i in g:
    if i not in k:
        k.append(i)
if a<3:
    print(k[-1])
else:
    print(k[-3])