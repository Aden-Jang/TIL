N=int(input())
for i in range(1,N+1):
    a=list(input())
    b=list(reversed(a))
    if a==b:
        print("#",i," 1",sep="")
    else:
        print("#",i," 0",sep="")