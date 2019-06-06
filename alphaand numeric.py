x=input()
a1=a2=0
for i in x:
    if i.isalpha():
        a2+=1
    elif i.isnumeric():
        a1+=1
if a1>=1 and c2>=1:
    print('Yes')
else:
    print('No')
