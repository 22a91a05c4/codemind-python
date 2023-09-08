a=int(input())
for i in range(a):
    b=input()
    c=0
    for j in b:
        if j in "0123456789":
            c+=1
    if c>0:
        print("Yes",end="
")
    else:
        print("No",end="
")