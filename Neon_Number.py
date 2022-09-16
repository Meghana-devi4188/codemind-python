n=int(input())
a=n**2
sum=0
while a!=0:
    b=a%10
    a=a//10
    sum+=b
if sum==n:
    print("Neon Number")
elif sum!=n:
    print("Not Neon Number")