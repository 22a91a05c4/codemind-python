a=int(input())
for i in range(a):
    v=int(input())
    c=0
    for j in range(1,v+1):
        t=j*j
        if t==v:
            c+=1
    if c==1:
        print("True")
    else:
        print("False")