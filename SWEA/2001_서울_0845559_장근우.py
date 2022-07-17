T=int(input())
for i in range(1,T+1):
    N,M=map(int,input().split())
    f = []
    for _ in range(N):
        A = list(map(int, input().split()))
        f.append(A)
    cnt=0
    ans=0
    for j in range(N-M+1):
        for k in range(N-M+1):
            for l in range(M):
                for m in range(M):
                    cnt+=f[j+l][k+m]
            if cnt>=ans:
                ans=cnt
                cnt=0
            else:
                cnt=0
    print("#",i," ",ans,sep="")