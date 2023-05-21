a=int(input())
s=0
lst=list(map(int,input().split()))
for i in lst:
    if i<a:
        s+=1
if(s==a):
    print("YES")
else:
    print("NO")