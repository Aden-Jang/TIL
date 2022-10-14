di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def f(a, b):
    global alst
    q = []
    q.append((a, b))
    vis = [[0] * (N) for _ in range(N)]
    vis[a][b] = 1
    cnt = 1
    alst[a][b] = 2
    while q:
        x, y = q.pop(0)
        for i in range(4):
            if 0 <= x + di[i] < N and 0 <= y + dj[i] < N and vis[x + di[i]][y + dj[i]] == 0:
                if alst[x + di[i]][y + dj[i]] == 1:
                    q.append(((x + di[i]), (y + dj[i])))
                    vis[x + di[i]][y + dj[i]] = 1
                    alst[x + di[i]][y + dj[i]] = 2
                    cnt += 1
    return cnt



N = int(input())
alst = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        alst[i][j] = int(alst[i][j])
anslst = []
for i in range(N):
    for j in range(N):
        if alst[i][j] == 1:
            anslst.append(f(i, j))
anslst.sort()
print(len(anslst))
print(*anslst, sep="\n")
