def f(n, sm):
    global ans
    if ans <= sm:
        return
    if n == N:
        ans = min(ans, sm)
        return
    for j in range(N):
        if vis[j] == 0:
            vis[j] = 1
            f(n+1, sm+a[n][j])
            vis[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    vis = [0] * N
    ans = 100 * N
    f(0,0)
    print(f'#{tc} {ans}')