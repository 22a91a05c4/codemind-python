s=input()
ma=0
c=0
for i in s:
    if i in "aeiou":
        c+=1
        ma=max(c,ma)
    else:
        c=0
print(ma)