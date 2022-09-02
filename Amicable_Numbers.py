x=int(input())
y=int(input())
a=1
b=1
s1=0
s2=0
while a<x and b<y:
    if x%a==0:
        s1+=a
    if y%b==0:
        s2+=b
    a+=1
    b+=1
if s1==y and s2==x:
    print("Amicable")
else:
    print("Not Amicable")
