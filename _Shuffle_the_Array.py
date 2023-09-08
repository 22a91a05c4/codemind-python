a=int(input())
ls=list(map(int,input().split()))
h=int(input())
t=[]
k=[]
m=[]
for i in range(0,h):
    t.append(ls[i])
for j in range(h,a):
    k.append(ls[j])
for i in range(len(t)):
    m.append(t[i])
    m.append(k[i])
print(*m)