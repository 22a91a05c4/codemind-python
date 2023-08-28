ls=list(map(str,input().split()))
c=0
for i in range(len(ls)):
    if ls[i][0] in "aeiouAEIOU":
        if ls[i][-1] not in "aeiouAEIOU":
            c+=1
print(c)