m,nb=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
g=[]
for i in l:
    if i not in l1:
        g.append(i)
for i in l1:
    if i not in l:
        g.append(i)
print(*g)