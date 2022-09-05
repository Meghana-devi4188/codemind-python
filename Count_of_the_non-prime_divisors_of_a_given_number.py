def prime(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
        if count>2:
            return a
n=int(input())
countl=1
for i in range(1,n+1):
    if n%i==0:
        num=prime(i)
        if num!=None:
            countl+=1
print(countl)