n=int(input())
m=int(input())
y=m+n+1
z=(m+n)**(m+n)
for i in range(y,z):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        k=i
        break
print(k-(m+n))