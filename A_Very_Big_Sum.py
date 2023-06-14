k=int(input())
s=0
ls=list(map(int,input().split()))
for i in range(len(ls)):
    s=s+ls[i]
print(s)