def f(i, k, s):
    global minV
    if i == k:
        if minV > s:
            minV = s
    elif s >= minV:
        return
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s + a[i][p[i]])
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    minV = N * 10
    f(0, N, 0)
    print(f'#{tc} {minV}')