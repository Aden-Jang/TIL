di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)
def bfs(n):
    global ans
    while q:
        x, y = q.pop(0)
        vis[x][y] = 1
        if x == y == n:
            return
        for i in range(4):
            if 0 <= x+di[i] <= n and 0 <= y+dj[i] <= n:
                a[x+di[i]][y+dj[i]] = min(anlst[x+di[i]][y+dj[i]], a[x+di[i]][y+dj[i]] + a[x][y])
                if vis[x + di[i]][y + dj[i]] == 0:
                    q.append((x+di[i], y+dj[i]))
                    vis[x+di[i]][y+dj[i]] = 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a[i][j] = int(a[i][j])
    anlst = [[1000] * N for _ in range(N)]
    x, y = 0, 0
    q = []
    q.append((x, y))
    vis = [[0] * N for _ in range(N)]
    ans = 0
    bfs(N-1)
    print(*a, sep='\n')