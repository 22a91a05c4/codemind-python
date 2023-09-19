a=list(map(str,input().split()))
l=[]
for i in a:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    l.append(c)
g=max(l)
f=0
for i in range(len(l)):
    if l[i]==g:
        f+=1
print(f)