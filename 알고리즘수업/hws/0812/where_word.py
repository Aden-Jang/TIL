T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N-K+1):
            if N == K:
                if a[i][j:j + K] == [1] * K:
                    ans += 1
            elif j == 0 and a[i][j] == 1:
                if a[i][j:j+K] == [1] * K and a[i][j+K] == 0:
                    ans += 1
            elif j == N-K and a[i][j] == 1 and a[i][j-1] == 0:
                if a[i][j:j+K] == [1] * K:
                    ans += 1
            elif a[i][j] == 1 and a[i][j-1] == 0:
                if a[i][j:j+K] == [1] * K and a[i][j+K] == 0:
                    ans += 1
    for i in range(N):
        for j in range(N-K+1):
            if N == K:
                if a[j:j + K][i] == [1] * K:
                    ans += 1
            elif j == 0 and a[i][j] == 1:
                if a[i][j:j+K] == [1] * K and a[i][j+K] == 0:
                    ans += 1
            elif j == N-K and a[i][j] == 1 and a[i][j-1] == 0:
                if a[i][j:j+K] == [1] * K:
                    ans += 1
            elif a[i][j] == 1 and a[i][j-1] == 0:
                if a[i][j:j+K] == [1] * K and a[i][j+K] == 0:
                    ans += 1

    print(f'#{tc} {ans}')
