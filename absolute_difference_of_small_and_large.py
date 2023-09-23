a=list(map(str,input().split()))
for i in range(0,len(a)):
   h=min(a[i])
   n=max(a[i])
   v=(ord(n))-(ord(h))
   print(v,end=" ")