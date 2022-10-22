n=int(input())
arr=list(map(int,input().split()))
m=0
for i in range(n):
    m+=arr[i]
print(m)