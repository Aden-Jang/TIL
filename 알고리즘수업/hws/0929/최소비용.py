def bfs(si, sj):
    q = []
    s = [[INF] * N for _ in range(N)]

    q.append((si, sj))
    s[si][sj] = 0

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and s[ni][nj] > s[ci][cj] + 1 + max(0, a[ni][nj] - a[ci][cj]):
                s[ni][nj] = s[ci][cj] + 1 + max(0, a[ni][nj] - a[ci][cj])
                q.append((ni, nj))

    return s[N - 1][N - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    INF = 100*1000
    ans = bfs(0, 0)
    print(f'#{tc} {ans}')
