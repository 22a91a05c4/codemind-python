a=int(input())
n=int(input())
for i in range(n):
    g,h=map(int,input().split())
    if g<a or h<a:
        print("UPLOAD ANOTHER")
    else:
        if g==h:
            print("ACCEPTED")
        else:
            print("CROP IT")