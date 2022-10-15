t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=[]
    for i in arr:
        if i%2==1:
           a.append(i)
    if len(a)==0:
       print(0)
    elif len(a)>0:
        print(len(a)//2)
    else:
        print((len(a)-1//2))