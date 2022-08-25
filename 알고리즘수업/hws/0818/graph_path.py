T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    a = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        a[s].append(e)
    S, G = map(int, input().split())
    ans = 0
    vis = [0] * (V+1)
    stack = [0] * (V+1)
    v = S
    top = -1
    vis[v] = 1
    while True:
        if v == G:
            ans = 1
            break
        for i in a[v]:
            if i == 0:
                continue
            elif vis[i] == 0:
                top += 1
                stack[top] = v
                v = i
                vis[i] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break

    print(f'#{tc} {ans}')