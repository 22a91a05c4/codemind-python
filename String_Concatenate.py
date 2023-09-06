s1=input()
s2=input()
l=[]
for i in s1:
    l.append(i)
for j in s2:
    l.append(j)
k=sorted(l)
print("".join(k))