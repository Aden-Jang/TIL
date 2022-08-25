T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    i = 0
    ans = 0
    while i <= N//2:
        if i != N//2:
            ulst = a[i][N//2-i:N//2+i+1]
            dlst = a[-i-1][N//2-i:N//2+i+1]
            for j in ulst:
                ans += j
            for j in dlst:
                ans += j
        elif i == N//2:
            lst = a[i]
            for j in lst:
                ans += j
        i += 1
    print(f'#{tc} {ans}')