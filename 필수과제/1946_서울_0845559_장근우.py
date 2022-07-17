T=int(input())
for j in range(1,T+1):
    N=int(input())
    A=''
    for i in range(N):
        a,b=map(str,input().split())
        A=A+(a*int(b))
    print("#", j,sep="")
    for k in range(len(A)):
        if k %10==9 or k == len(A)-1:
            print(A[k])
            print('',end='')
        else:
            print(A[k],end='')