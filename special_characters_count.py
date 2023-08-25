a=input()
c=[]
s=0
for i in range(len(a)):
    if a[i] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        c.append(a[i])
for j in range(len(c)):
    if c[j]!=" ":
        s+=1
print(s)