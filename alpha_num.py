str=input()
a=0
b=0
for i in str:
    if i.isalpha():
        a+=1
    elif i.isnumeric():
        b+=1
if(a>=1 and b>=1):
    print("Yes")
else:
    print("No")
