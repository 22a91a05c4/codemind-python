ls=list(map(str,input().split()))
k=[]
s=0
for i in range(len(ls)):
    b=len(ls[i])
    k.append(b)
for j in range(len(k)):
    s=s+k[j]
print(s)