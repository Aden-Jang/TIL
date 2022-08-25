for _ in range(10):
    tc = int(input())
    a = [list(map(int, input())) for _ in range(16)]
    vis = [[0] * (16) for _ in range(16)]
    for i in range(16):
        for j in range(16):
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
            vis[x + 1][y] = 1
        if a[x - 1][y] == 0 and vis[x - 1][y] == 0:
            q.append([x - 1, y])
            vis[x - 1][y] = 1
        if a[x][y + 1] == 0 and vis[x][y + 1] == 0:
            q.append([x, y + 1])
            vis[x][y + 1] = 1
        if a[x][y - 1] == 0 and vis[x][y - 1] == 0:
            q.append([x, y - 1])
            vis[x][y - 1] = 1
        if q == []:
            ans = 0
    print(f'#{tc} {ans}')