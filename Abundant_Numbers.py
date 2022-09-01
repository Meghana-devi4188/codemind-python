a=int(input())
i=1
s=0
while i<a:
    if a%i==0:
        s+=i
    i+=1
if s>a:
    print("True")
else:
    print("False")