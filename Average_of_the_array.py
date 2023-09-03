a=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(a):
    c=c+ls[i]
avg=c/a
print("%.2f"%(avg))