T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly=0
            for k in range(i,M+i):
                for l in range(j,j+M):
                    fly += a[k][l]
            if fly >= ans:
                ans = fly
    print(f'#{tc} {ans}')