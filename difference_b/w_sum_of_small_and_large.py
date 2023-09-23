a=list(map(str,input().split()))
s=0
c=0
for i in range(0,len(a)):
   h=min(a[i])
   n=max(a[i])
   s=s+(ord(n))
   c=c+(ord(h))
b=s-c
print(b)