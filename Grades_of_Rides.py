a,bc,d=map(int,input().split())
if a>50 and bc>60 and d>100:
    print(10)
elif a>50 and bc>60:
    print(9)
elif bc>60 and d>100:
    print(8)
elif a>50 and d>100:
    print(7)
elif(a>50 or bc>60 or d>100):
    print(6)
else:
    print(5)