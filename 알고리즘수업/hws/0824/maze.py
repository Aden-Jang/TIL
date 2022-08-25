def bfs(i, j, N):
    q = [(i,j)]
    vis = [[0] * N for _ in range(N)]
    vis[i][j] = 1
    while q:
        i, j = q.pop(0)
        if a[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and a[ni][nj] != 1 and vis[ni][nj] == 0:
                q.append((ni, nj))
                vis[ni][nj] = vis[i][j] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if a[i][j] == 2:
                break
    print(f'#{tc} {bfs(i, j, N)}')