a=input()
l=[]
for i in a:
    c=0
    for j in a:
        if j==i:
            c=c+1
    if c==1:
        l.append(c)
if len(l)==len(a):
    print("Unique Number")
else:
    print("Not Unique Number")