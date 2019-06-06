n,m=map(int,input().split())
a=map(int,input().split())
l=0
for i in a:
	if(i==m):
		l=l+1
if(l>0):
	print("yes")
else:
	print("no")
