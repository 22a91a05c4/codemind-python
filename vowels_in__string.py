n=input()
c=0
k=[]
b=[]
h=[]
v=["A","E","I","O","u","a","e","i","o","u"]
for i in range(len(n)):
    k.append(n[i])
for i in range(len(n)):
    for j in range(len(v)):
        if k[i]==v[j]:
          c+=1
          b.append(k[i])
for i in range(len(b)):
    if b[i] not in h:
        h.append(b[i])
if c==0:
    print("-1")
else:
    print(*h)