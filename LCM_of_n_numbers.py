import math
a=int(input())
b=list(map(int,input().split()))
d=1
for i in range(a):
    s=b[i]
    d=math.lcm(s,d)
    i+=1
print(d)