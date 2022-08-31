x=int(input())
for i in range(x):
    x1=int(input())
    m=[int(i)for i in input().split()]
    m1=sorted(m)
    if m==m1:
        print(0)
    else:
        print(max(m1)-min(m1))