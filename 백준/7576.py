from collections import deque

M, N = map(int, input().split())
to = deque(deque(map(int, input().split())) for _ in range(N))
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
q = deque()
vis = deque([0] * M for _ in range(N))
for i in range(N):
    for j in range(M):
        if to[i][j] == 1:
            q.append((i,j))
            vis[i][j] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        if 0 <= x+di[i] < N and 0 <= y+dj[i] < M:
            if to[x+di[i]][y+dj[i]] == 0 and vis[x+di[i]][y+dj[i]] == 0:
                to[x + di[i]][y + dj[i]] = 1
                vis[x + di[i]][y + dj[i]] = vis[x][y] + 1
                q.append((x + di[i], y + dj[i]))

for i in range(N):
    for j in range(M):
        if to[i][j] == 0:
            break
    if to[i][j] == 0:
        print(-1)
        break
else:
    print(vis[x][y] - 1)