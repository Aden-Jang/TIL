def f(i, k, s):
    global M
    global cnt
    global vis
    if cnt == N-1:
        M = min(M, s+a[i][0])
        return
    elif s >= M:
        return
    else:
        for d in range(k):
            if vis[d] == 1:
                continue
            else:
                cnt += 1
                vis[d] = 1
                f(d, k, s + a[i][d])
                cnt -= 1
                vis[d] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    M = 100 * N
    cnt = 0
    vis = [0] * N
    vis[0] = 1
    f(0, N, 0)
    print(f'#{tc} {M}')