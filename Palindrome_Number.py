a=int(input())
for i in range(1,a+1):
    b=int(input())
    t=b
    s=0
    while b:
        r=b%10
        s=(s*10)+r
        b=b//10
    if t==s:
        print("True")
    else:
        print("False")