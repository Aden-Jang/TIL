T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    a.append([1] * (N+2))
    a.insert(0, [1] * (N+2))
    vis = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(N+2):
        for j in range(N+2):
            if a[i][j] == 2:
                x, y = i, j
                break
    q = []
    q.append([x, y])
    while q:
        x, y = q.pop(0)
        if a[x + 1][y] == 3 or a[x - 1][y] == 3 or a[x][y + 1] == 3 or a[x][y - 1] == 3:
            ans = vis[x][y]
            break
        if a[x + 1][y] == 0 and vis[x + 1][y] == 0:
            q.append([x + 1, y])
            vis[x + 1][y] = vis[x][y] + 1
        if a[x - 1][y] == 0 and vis[x - 1][y] == 0:
            q.append([x - 1, y])
            vis[x - 1][y] = vis[x][y] + 1
        if a[x][y + 1] == 0 and vis[x][y + 1] == 0:
            q.append([x, y + 1])
            vis[x][y + 1] = vis[x][y] + 1
        if a[x][y - 1] == 0 and vis[x][y - 1] == 0:
            q.append([x, y - 1])
            vis[x][y - 1] = vis[x][y] + 1
        if q == []:
            ans = 0
    print(f'#{tc} {ans}')