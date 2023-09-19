a=list(map(str,input().split()))
l=[]
for i in a:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    l.append(c)
print(min(l))