def f(n, a, x, y):
    q = []
    q.append([x,y])
    r = 1
    o, p = x, y
    while q:
        x, y = q.pop(0)
        for i in range(4):
            if 0 <= x+di[i] < n and 0 <= y+dj[i] < n:
                if a[x+di[i]][y+dj[i]] == a[x][y] + 1:
                    x, y = x+di[i], y+dj[i]
                    q.append([x, y])
                    r += 1
                    break
    return a[o][p], r

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)
T = int(input())
for tc in range(1, T+1):
    ffn, froom = 0, 0
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            fn, room = f(N, a, i, j)
            if room > froom:
                ffn, froom = fn, room
            elif room == froom:
                if ffn > fn:
                    ffn = fn

    print(f'#{tc} {ffn} {froom}')
