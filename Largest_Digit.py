n=int(input())
temp=0
while n>0:
    r=n%10
    if temp>r:
        temp=temp
    else:
        temp=r
    n//=10
print(temp)