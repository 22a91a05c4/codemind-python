a=int(input())
t=a
e=0
o=0
while(a):
    r=a%10
    if r%2==0:
        e+=1
    else:
        o+=1
    a=a//10
if e==len(str(t)):
    print("Even")
elif o==len(str(t)):
    print("Odd")
else:
    print("Mixed")