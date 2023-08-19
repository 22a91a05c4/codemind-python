n=list(map(str,input().split()))
k=[]
for i in range(0,len(n)):
    k.append(len(n[i]))
print(*k)