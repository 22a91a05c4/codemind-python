a=input()
l=a[::-1]
c=0
for i in range(len(a)):
    if l[i]==a[i] or l[i]==a[i].upper() or l[i]==a[i].lower():
        c+=1
if c==len(a):
    print("True")
else:
    print("False")