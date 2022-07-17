T=int(input())
for i in range(1,T+1):
    N,K=map(int,input().split())
    p=[]
    for _ in range(N):
        A = list(map(int, input().split()))
        p.append(A)
    ans=0
    for j in range(N):
        cnt=0
        for k in range(N):
            if p[j][k]==1 and k!=N-1:
                cnt+=1
            elif p[j][k]==1 and k==N-1:
                cnt += 1
                if cnt == K:
                    ans+=1
                    cnt=0
                else:
                    cnt=0
            else:
                if cnt == K:
                    ans+=1
                    cnt=0
                else:
                    cnt=0
    for j in range(N):
        cnt = 0
        for k in range(N):
            if p[k][j] == 1 and k != N - 1:
                cnt += 1
            elif p[k][j]==1 and k==N-1:
                cnt += 1
                if cnt == K:
                    ans+=1
                    cnt=0
                else:
                    cnt=0
            else:
                if cnt == K:
                    ans += 1
                    cnt = 0
                else:
                    cnt=0
    print("#",i," ",ans,sep='')