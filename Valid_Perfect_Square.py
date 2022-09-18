h=int(input())
for i in range(h):
    def perf(n):
        for i in range(0,n):
            res=i*i
            if res==n:
                return 1
    n=int(input())
    a=perf(n)
    if a==1:
        print("True")
    else:
        print("False")