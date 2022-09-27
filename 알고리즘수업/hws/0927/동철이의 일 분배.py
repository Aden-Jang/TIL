def f(n, d):
    global ans
    if n == N:
        ans = max(ans, d)
        return

    if d <= ans:
        return

    for j in range(N):
        if vis[j] == 0:
            vis[j] = 1
            f(n+1, d*a[n][j]*0.01)
            vis[j] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    vis = [0] * N
    ans = 0
    f(0, 1)

    print(f'#{tc} {ans*100:.6f}')