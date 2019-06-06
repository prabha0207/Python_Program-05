a1,a2=map(int,input().split())
l = list()
for x in range(a1,a2+1):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        l.append(x)
print(len(l)
