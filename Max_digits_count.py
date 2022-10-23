n=int(input())
l=list(map(str,input().split()))
q=[]
for i in l:
    q.append(len(i))
print(q.count(max(q)))
    