x=int(input())
a=0
b=0
if x<0:
    x=-x
    a=1
else:
    x=x
    a=0
while x!=0:
    r=x%10
    b=(b*10)+r
    x=x//10
if a==1:
    print(-b)
else:
    print(b)