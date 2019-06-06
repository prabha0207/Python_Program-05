a,b=list(map(int,input().split()))
l=list(map(int,input().split()))
c=0
for i in l:
    if (int(i)==b):
        c+=1
if(c>=1):
    print("yes")
else:
    print("no")
