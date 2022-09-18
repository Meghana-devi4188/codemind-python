def fact(n):
    if n==0 or n==1:
        return 1
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
a=int(input())
num=a
sum=0
while a!=0:
    rem=a%10
    a//=10
    sum+=fact(rem)
if num==sum:
    print("The number",num,"is a strong number")
elif num!=sum:
    print("The number",num,"is not a strong number")