x=int(input())
m=0
while(x>0):
    dig=x%10
    m=m+dig
    x=x//10
print(m)
