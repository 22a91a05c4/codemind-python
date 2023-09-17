l=list(map(int,input().split()))
k=list(map(int,input().split()))
s=0
c=0
for i in range(0,3):
    if l[i]>k[i]:
        s+=1
    elif l[i]<k[i]:
        c+=1
print(s,c)