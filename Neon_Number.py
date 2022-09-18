m=int(input())
s=m*m
b=0
while(s>0):
    a=s%10
    b=b+a
    s=s//10
if b==m:
    print("Neon Number")
else:
    print("Not Neon Number")