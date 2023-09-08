a=int(input())
for i in range(a):
    s=input()
    r=s[::-1]
    if r==s:
        print("YES",end=" ")
        d=len(s)
        if d%2==0:
            print("EVEN",end="
")
        else:
            print("ODD",end="
")
    else:
        print("NO",end="
")