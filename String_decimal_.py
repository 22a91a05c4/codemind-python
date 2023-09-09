a=int(input())
for i in range(a):
    b=input()
    c=0
    for i in b:
        if i in "1234567890":
            c+=1
    if c==(len(b)):
        print("True")
    else:
        print("False")