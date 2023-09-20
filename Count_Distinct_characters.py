a=input()
l=[]
for i in a:
    if i in "abcdefghijklmnopqrstuvwxyz":
            l.append(i)
k=set(l)
print(len(k))