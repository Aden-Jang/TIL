def dfs(n):
    if vis[n] == 1:
        return
    vis[n] = 1
    ans.append(n)

    for j in range(1, V+1):
        if a[n][j] == 1:
            dfs(j)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    a = [[0]*(V+1) for _ in range(V+1)]
    vis = [0] * (V+1)
    for _ in range(E):
        s, e = map(int, input().split())
        a[s][e] = a[e][s] = 1

    ans = []
    dfs(1)
    print(f'#{tc}', end=' ')
    print(*ans)