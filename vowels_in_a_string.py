n=input()
x=input()
c=0
for i in range(len(n)):
    if x==n[i]:
        m=i
        c+=1
        break
if c>0:
    print("True")
    print(m)
else:
    print("False")