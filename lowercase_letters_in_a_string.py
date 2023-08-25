a=input()
c=0
for i in range(len(a)):
    if a[i] in "abcdefghijklmnopqrstuvwxyz":
        c+=1
print(c)