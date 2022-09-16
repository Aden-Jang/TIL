di = (1, -1, 0, 0, 1, 1, -1, -1)
dj = (0, 0, 1, -1, 1, -1, 1, -1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = [[0] * N for _ in range(N)]
    a[N//2-1][N//2-1] = a[N//2][N//2] = 2
    a[N//2][N//2-1] = a[N//2-1][N//2] = 1

    for i in range(M):
        x, y, d = map(int, input().split())
        a[x-1][y-1] = d
        for j in range(8):
            p, q = x-1, y-1
            if 0 <= p+di[j] < N and 0 <= q+dj[j] < N:
                if d == 1:
                    if a[p + di[j]][q + dj[j]] == 2:
                        cnt = 1
                        while True:
                            p, q = p + di[j], q + dj[j]
                            cnt += 1
                            if 0 > p+di[j] or p+di[j] >= N or 0 > q+dj[j] or q+dj[j] >= N or a[p+di[j]][q+dj[j]] == 0:
                                break
                            elif a[p+di[j]][q+dj[j]] == 1:
                                for k in range(cnt):
                                    a[x+(di[j]*k)-1][y+(dj[j]*k)-1] = 1
                                break
                elif d == 2:
                    if a[p + di[j]][q + dj[j]] == 1:
                        cnt = 1
                        while True:
                            p, q = p + di[j], q + dj[j]
                            cnt += 1
                            if 0 > p+di[j] or p+di[j] >= N or 0 > q+dj[j] or q+dj[j] >= N or a[p+di[j]][q+dj[j]] == 0:
                                break
                            elif a[p+di[j]][q+dj[j]] == 2:
                                for k in range(cnt):
                                    a[x+(di[j]*k)-1][y+(dj[j]*k)-1] = 2
                                break
    w = b = 0
    for i in range(N):
        for j in range(N):
            if a[i][j] == 1:
                b += 1
            elif a[i][j] == 2:
                w += 1
    print(f'#{tc} {b} {w}')
