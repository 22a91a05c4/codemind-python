a=int(input())
c=0
for i in range(1,a+1):
    if i*i==a:
        c+=1
if c==1:
    print("True")
else:
    print("False")