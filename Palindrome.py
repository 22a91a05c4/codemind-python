a=int(input())
s=0
t=a
while a:
    r=a%10
    s=s*10+r
    a=a//10
if s==t:
    print("True")
else:
    print("False")