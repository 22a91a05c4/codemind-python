a,b=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
c=[]
for i in range(a):
    for j in range(b):
        if l[i]==s[j]:
            c.append(s[j])
v=set(c)
print(len(v))