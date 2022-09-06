a=int(input())
count=0
while a!=0:
    b=a%10
    a=a//10
    count+=1
if count==10:
    print("Valid")
else:
    print("Invalid")