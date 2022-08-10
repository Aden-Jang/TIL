T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = []
    ans = 0
    for i in range(N):
        aa = list(map(int,input().split()))
        aa.insert(0,aa[0])
        aa.append(aa[-1])
        if i == 0 or i == N-1:
            a.append(aa)
        a.append(aa)
    for i in range(1,N+1):
        for j in range(1,N+1):
            ans += abs(a[i][j]-a[i][j-1])
            ans += abs(a[i][j]-a[i][j+1])
            ans += abs(a[i][j]-a[i-1][j])
            ans += abs(a[i][j]-a[i+1][j])
    print(f'#{tc} {ans}')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            for (di,dj) in ((-1,0),(1,0),(0,-1),(0,1)):
                ni = i+di
                nj = j+dj
                if 0<=ni<N and 0<=nj<N:
                    ans += abs(a[i][j]-a[ni][nj])
    print(f'#{tc} {ans}')
