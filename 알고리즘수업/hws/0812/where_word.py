def find_lst(N, K, a):
    ans = 0
    for i in range(N):
        for j in range(N-K+1):
            if N == K:
                if a[i][j:j + K] == [1] * K:
                    ans += 1
            elif a[i][j] == 1:
                if j == 0:
                    if a[i][j:j+K] == [1] * K and a[i][j+K] == 0:
                        ans += 1
                elif j == N-K and a[i][j-1] == 0:
                    if a[i][j:j+K] == [1] * K:
                        ans += 1
                elif a[i][j-1] == 0:
                    if a[i][j:j+K] == [1] * K and a[i][j+K] == 0:
                        ans += 1
    return ans

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    ans1 = find_lst(N, K, a)
    for i in range(N):
        for j in range(N):
            if i < j:
                a[i][j], a[j][i] = a[j][i], a[i][j]
    ans2 = find_lst(N, K, a)
    ans = ans1 + ans2
    print(f'#{tc} {ans}')
