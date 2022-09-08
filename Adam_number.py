def reve(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
n=int(input())
r=reve(n)
r*=r
r=reve(r)
if n*n==r:
    print("True")
else:
    print("False")