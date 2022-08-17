T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    lst = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)

    ans = '1'
    vis = [0] * N
    stack = [0] * N
    top = -1
    v = 1
    vis[v] = 1
    while True:
        for i in lst[v]:
            if i == 0:
                continue
            elif vis[i] == 0:
                top += 1
                stack[top] = v
                v = i
                ans = ans + ' ' + str(v)
                vis[i] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break
    print(f'#{tc} {ans}')