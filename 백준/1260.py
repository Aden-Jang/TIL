def dfs(a, i):
    global dfsl
    if visit[i] == 1:
        return
    visit[i] = 1
    dfsl.append(i)

    for j in a[i]:
        if visit[j] == 0:
            dfs(a, j)


def bfs(a):
    global bfsl
    q = []
    q.append(V)
    vis = [0] * (N+1)
    vis[V] = 1
    bfsl.append(V)
    while q:
        x = q.pop(0)
        for i in a[x]:
            if vis[i] == 0:
                q.append(i)
                bfsl.append(i)
                vis[i] = 1



N, M, V = map(int, input().split())
a = [[] for _ in range(N+1)]
for i in range(M):
    p, c = map(int, input().split())
    a[p].append(c)
    a[c].append(p)
for i in range(len(a)):
    a[i].sort()
visit = [0] * (N+1)
dfsl = []
bfsl = []

dfs(a, V)
bfs(a)
print(*dfsl, sep=' ')
print(*bfsl, sep=' ')