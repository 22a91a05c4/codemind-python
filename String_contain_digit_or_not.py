a=input()
c=0
for i in a:
    if i in"1234567890":
        c+=1
if c>0:
    print("Contains {} digit".format(c))
else:
    print("Doesn't contain digit")