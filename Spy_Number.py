n=int(input())
a=1
b=0
while n>0:
    r=n%10
    a*=r
    b+=r
    n//=10
if a==b:
    print("Spy Number")
else:
    print("Not Spy Number")