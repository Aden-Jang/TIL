T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    for i, j in a:
        lst[i].append(j)
        lst[j].append(i)
    q = [S]
    vis = [0] * (V+1)
    vis[S] = 1

    while q:
        S = q.pop(0)
        for i in lst[S]:
            if vis[i] == 0:
                q.append(i)
                vis[i] = vis[S] + 1
        if S == G:
            break
    if S == G:
        ans = vis[S]-1
    else:
        ans = 0
    print(f'#{tc} {ans}')