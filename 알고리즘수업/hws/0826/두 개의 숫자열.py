T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    if N <= M:
        for i in range(M - N + 1):
            x = 0
            for j in range(N):
                x += ai[j] * bj[i+j]
            if i == 0:
                ans = x
            else:
                if ans < x:
                    ans = x
    else:
        for i in range(N - M + 1):
            x = 0
            for j in range(M):
                x += bj[j] * ai[i+j]
            if i == 0:
                ans = x
            else:
                if ans < x:
                    ans = x
    print(f'#{tc} {ans}')