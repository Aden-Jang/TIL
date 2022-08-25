T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(input().split()) for _ in range(N)]
    ans = ['' for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[i] = str(ans[i]) + str(a[N - j - 1][i])
        ans[i] = str(ans[i]) + ' '
    for i in range(N):
        for j in range(N):
            ans[i] = str(ans[i]) + str(a[N - i - 1][N - j - 1])
        ans[i] = str(ans[i]) + ' '
    for i in range(N):
        for j in range(N):
            ans[i] = str(ans[i]) + str(a[j][N - i- 1])
    print(f'#{tc}')
    print(*ans, sep='\n')