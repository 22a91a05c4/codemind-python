a=input()
l=[]
k=[]
for i in a:
    if i in "abcdefghijklmnopqrstuvwxyz":
            l.append(i)
for i in l:
    if i not in k:
        k.append(i)
d=sorted(k)
for i in d:
    print(i,end="")