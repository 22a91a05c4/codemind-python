n=int(input())
ls=[]
while n:
    r=n%10
    ls.append(r)
    n=n//10
c=0
for i in range(0,len(ls)):
    if ls[i]==1:
        c+=1
print(c)