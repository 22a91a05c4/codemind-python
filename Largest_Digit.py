a=int(input())
ls=[]
while a:
    r=a%10
    ls.append(r)
    a=a//10
print(max(ls))