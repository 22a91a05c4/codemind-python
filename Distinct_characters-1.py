a=input()
l=[]
for i in a:
    c=0
    for j in a:
        if j==i:
            c+=1
    if c==1:
        if i in "abcdefghijklmnopqrstuvwxyz":
            l.append(i)
k=sorted(l)
for i in k:
    print(i,end="")