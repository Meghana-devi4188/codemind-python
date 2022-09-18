def s(n):
    for i in str(n):
      i=int(i)
      if i==0:
         return False
      if n%i==0:
         a=True
      else:
        a=False
        break
    return a
a=int(input())
b=int(input())
for i in range(a,b+1):
    r=s(i)
    if r==True:
       print(i,end=' ')