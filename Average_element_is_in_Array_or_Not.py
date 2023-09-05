a=int(input())
ls=list(map(int,input().split()))
c=0
f=0
for i in range(a):
    c=c+ls[i]
avg=c//a
for i in range(a):
    if avg==ls[i]:
        f+=1
if f>0:
    print("True")
else:
    print("False")