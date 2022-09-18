a=int(input())
q=[int(i) for i in input().split(" ")]
m,n=[int(i) for i in input().split(" ") ]
s=0
for ele in q:
    if ele<m or ele>n:
        s=s+ele
print(s)