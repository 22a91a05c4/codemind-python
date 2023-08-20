n=list(map(str,input().split()))
k=[]
m=len(n)
i=m-1
while(i>=0):
    k.append(n[i])
    i=i-1
print(*k)