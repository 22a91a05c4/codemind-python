a=int(input())
ls=list(map(int,input().split()))
s=0
for i in ls:
    s=s+i
k=s/a
print("%.2f"%(k))