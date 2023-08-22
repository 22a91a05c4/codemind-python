a=int(input())
ls=list(map(str,input().split()))
k=[]
c=0
for i in range(0,a):
    m=len(ls[i])
    k.append(m)
b=min(k)
for i in range(len(k)):
    if k[i]==b:
        c+=1
print(c)