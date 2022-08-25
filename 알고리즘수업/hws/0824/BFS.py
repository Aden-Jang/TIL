T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    a = {}
    for i in range(1, V+1):
        a[i] = []
    for _ in range(E):
        s, l = map(int, input().split())
        a[s] = a[s] + [l]
        a[l] = a[l] + [s]

    s = 1
    q = [1]
    vis = [0] * (V+1)
    vis[1] = 1
    ans = ''
    while q:
        t = q.pop(0)
        if t == s:
            ans = str(t)
        else:
            ans = ans + ' ' + str(t)
        for i in a[t]:
            if not vis[i]:
                q.append(i)
                vis[i] = 1
    print(f'#{tc} {ans}')