x=int(input())
count=0
for i in range(2,x):
    if x%i==0:
        count+=1
if count==0:
        print("prime")
else:
        print("not a prime")
        