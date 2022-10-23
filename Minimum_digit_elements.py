n=int(input())
l=list(map(str,input().split()))
b=[]
for i in l:
    b.append(len(i))
print(b.count(min(b)))
    