a=int(input())
sq=a*a
s=0
while sq:
    r=sq%10
    s=s+r
    sq=sq//10
if(a==s):
    print("Neon Number")
else:
    print("Not Neon Number")