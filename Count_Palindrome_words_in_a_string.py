a=list(map(str,input().split()))
k=[]
for i in range(len(a)):
    l=a[i][::-1]
    c=0
    for j in range(len(l)):
        if l[j]==a[i][j] or l[j]==a[i][j].upper() or l[j]==a[i][j].lower():
            c+=1
    if c==len(a[i]):
        k.append(a[i])
print(len(k))