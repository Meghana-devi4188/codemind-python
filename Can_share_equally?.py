a,b=map(int,input().split())
s=((a*1)+(b*2))
if a==0 and b%2==0:
    print('YES')
elif a==0 and b%2!=0:
    print('NO')
elif s%2==0:
    print('YES')
else:
    print('NO')
    