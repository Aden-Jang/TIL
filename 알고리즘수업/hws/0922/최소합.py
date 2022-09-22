di = (0, 1)
dj = (1, 0)
def f(x, y, s):
    global ans
    if s >= ans:
        return
    if x == y == N-1:
        ans = min(s, ans)
        return

    else:
        # if x < N-1:
        #     f(x+1, y, s + a[x+1][y])
        # if y < N-1:
        #     f(x, y+1, s + a[x][y+1])
        for i in range(2):
            x += di[i]
            y += dj[i]
            if x < N and y < N:
                f(x, y, s + a[x][y])
            x -= di[i]
            y -= dj[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N * 2
    f(0, 0, a[0][0])
    print(f'#{tc} {ans}')
