m,n=[int(i) for i in input().split()]
M=[]
for i in range(m):
    row=[int(j) for j in input().split()]
    M.append(row)
e_sum=0
o_sum=0
for i in range(m):
    for j in range(n):
        if M[i][j]%2==0:
           e_sum+=M[i][j]
        else:
            o_sum+=M[i][j]
print(e_sum,o_sum)