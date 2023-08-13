n=int(input())
k=[]
a=0
f=0
b=1
for i in range(0,n):
    c=a+b;
    k.append(c)
    a=b;
    b=c;
for i in range(0,n):
    if n==k[i]:
        f+=1
if f>0:
    print("True")
else:
    print("False")