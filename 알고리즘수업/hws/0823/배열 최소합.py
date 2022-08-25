def dfs(n, sm):
    global ans
    if sm >= ans: # 여태까지의 합이 이미 ans 보다 큰경우
        return
    if n == N:
        if ans > sm:
            ans = sm
        return
    for j in range(N):
        if not vis[j]:
            vis[j] = 1
            dfs(n+1, sm+a[n][j])
            vis[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N
    vis = [0] * N # 열의 개수만큼 필요
    dfs(0, 0)   # n==0 (0행), sum == 0

    print(f'#{tc} {ans}')

