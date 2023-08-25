a=input()
c=0
for i in range(len(a)):
    if a[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        c+=1
print(c)