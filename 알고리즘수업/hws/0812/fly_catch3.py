T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(N)]
    for j in range(M):
        for i in range(N):
            a[i].append(0*M)
            a[i].insert(0,0*M)
    for i in range(M):
        a.insert(0,[0]*(N+2*M))
        a.append([0]*(N+2*M))
    ans = 0
    for i in range(M,N+M):
        for j in range(M,N+M):
            fly = a[i][j]
            for k in range(1,M):
                fly += a[i][j+k]
                fly += a[i][j-k]
                fly += a[i+k][j]
                fly += a[i-k][j]
            if ans <= fly:
                ans = fly

    for i in range(M,N+M):
        for j in range(M,N+M):
            fly = a[i][j]
            for k in range(1,M):
                fly += a[i+k][j+k]
                fly += a[i+k][j-k]
                fly += a[i-k][j+k]
                fly += a[i-k][j-k]
            if ans <= fly:
                ans = fly

    print(f'#{tc} {ans}')
