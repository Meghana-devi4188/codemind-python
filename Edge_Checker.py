x,y=map(int,input().split())
if x>y:
    h=x
    s=y
elif y>x:
    h=y
    s=x
if s+1==h:
    print("Yes")
elif x==1 and y==10 or x==10 and y==1:
    print("Yes")
else:
    print("No")