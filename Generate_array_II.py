m=int(input())
l=list(map(int,input().split()))
g=[]
for i in range(0,m,2):
    for j in range(l[i+1]):
        print(l[i],end=' ')