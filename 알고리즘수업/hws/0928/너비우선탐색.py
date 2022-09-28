def bfs(s):
    q = []
    vis = [0] * (V+1)

    q.append(s)
    vis[s] = 1
    ans.append(s)

    while q:
        c = q.pop(0)
        for e in a1[c]:
            if vis[e] == 0:
                q.append(e)
                vis[e] = 1
                ans.append(e)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    a1 = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        a1[s].append(e)
        a1[e].append(s)
    for i in range(V+1):
        a1[i].sort()

    ans = []
    bfs(1)
    print(f'#{tc}', end=' ')
    print(*ans)