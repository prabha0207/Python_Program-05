x,y=input().split()
z=0
if len(x)!=len(y):
    print("no")
else:
    for i in range(len(x)):
        if x[i]!=y[i]:
            z+=1
if z==1:
    print("yes")
else:
    print("no")
