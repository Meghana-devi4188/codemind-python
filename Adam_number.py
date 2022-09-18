def rev(n):
    rev=0
    while n!=0:
        a=n%10
        rev=rev*10+a
        n//=10
    return rev
n=int(input())
sq=n*n
r=rev(n)
r*=r
s=rev(r)
if s==sq:
    print(True)
else:
    print(False)