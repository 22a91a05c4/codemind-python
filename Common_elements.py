a,b=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
c=[]
for i in range(a):
    for j in range(b):
        if l[i]==s[j]:
            c.append(s[j])
d=[]
for i in range(len(c)):
    if c[i] not in d:
        d.append(c[i])
print(*d)