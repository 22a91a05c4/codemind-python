n=list(map(str,input().split()))
k=[]
for i in range(0,len(n)):
    if i%2==0:
        m=n[i][::-1]
        k.append(m)
    else:
        k.append(n[i])
print(*k)