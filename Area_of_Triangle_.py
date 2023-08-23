import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
b=s*(s-a)*(s-b)*(s-c)
q=math.sqrt(b)
print("%.2f"%(q))