ls=list(map(str,input().split()))
t=[]
for i in range(len(ls)):
    k=ls[i][::-1]
    t.append(k)
print(*t)