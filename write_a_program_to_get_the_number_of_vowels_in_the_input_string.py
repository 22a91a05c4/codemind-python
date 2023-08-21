a=input()
v=["a","e","i","o","u","A","E","I","O","U"]
c=0
for i in range(len(a)):
    if a[i] in v:
        c+=1
if c==0:
    print("0")
else:
    print(c)