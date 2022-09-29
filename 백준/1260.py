def dfs(a, i):
    global dfsl
    vis = [0] * (N+1)
    dfsl.append(V)
    if vis[i] == 1:
        return
    vis[i] = 1

    for j in a[i]:
        if vis[j] == 0:
            dfsl.append(j)
            print(j)
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


for _ in range(10):
    N, M, V = map(int, input().split())
    a = [[] for _ in range(N+1)]
    for i in range(M):
        p, c = map(int, input().split())
        a[p].append(c)
        a[c].append(p)
    for i in range(len(a)):
        a[i].sort()

    dfsl = []
    bfsl = []
    dfs(a, V)
    bfs(a)
    print(dfsl)
    print(bfsl)