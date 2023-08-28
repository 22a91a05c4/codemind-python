a=input()
v=[]
s=[]
for i in a:
    if i in "aeiou":
        v.append(i)
    elif i in "AEIOU":
        s.append(i)
c1=set(v)
c2=set(s)
if len(c1)==5 or len(c2)==5:
    print("True")
else:
    print("False")