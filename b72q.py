x1=input()
s=0
l=['a','e','i','o','u','A','E','I','O','U']
for x in x1:
	if x in l:
		s=s+1
		break
if(s>0):
	print('yes')
else:
	print('no')
