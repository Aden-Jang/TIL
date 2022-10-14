di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
def f(a, b):
    q = []
    q.append((a, b))
    vis = [[0] * M for _ in range(N)]
    vis[0][0] = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            if 0 <= x+di[i] < N and 0 <= y+dj[i] < M and vis[x+di[i]][y+dj[i]] == 0:
                if alst[x+di[i]][y+dj[i]] == '1':
                    q.append((x+di[i], y+dj[i]))
                    vis[x + di[i]][y + dj[i]] = vis[x][y] + 1
                    if x + di[i] == N-1 and y + dj[i] == M-1:
                        return vis[x + di[i]][y + dj[i]]

N, M = map(int, input().split())
alst = [list(input()) for _ in range(N)]
print(f(0, 0))