a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        s=0
        for j in range(1,i+1):
            if i%j==0:
                s+=1
        if s>2:
            c+=1
print(c+1)