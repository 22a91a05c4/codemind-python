a=int(input())
ls=[]
c=0
s=0
while(a):
    r=a%10
    s+=1
    if r not in ls:
        ls.append(r)
        c+=1
    a=a//10
if c==s:
    print("Unique Number")
else:
    print("Not Unique Number")