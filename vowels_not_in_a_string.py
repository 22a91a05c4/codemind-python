a=input()
k=[]
v=["a","e","i","o","u"]
b=len(v)
c=0
for i in range(len(v)):
    if v[i] not in a:
        k.append(v[i])
    else:
        c+=1
if c==5:
    print("0")
else:
    print(*k)