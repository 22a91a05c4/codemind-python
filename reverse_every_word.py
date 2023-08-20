n=list(map(str,input().split()))
k=[]
for i in range(0,len(n)):
    b=n[i][::-1]
    k.append(b)
print(*k)