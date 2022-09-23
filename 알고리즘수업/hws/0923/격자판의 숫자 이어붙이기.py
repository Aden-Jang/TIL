di = (1, -1, 0, 0)
dj = (0, 0, 1, -1)

def f(x, y, st):
    global arr
    if len(st) == 7:
        if st not in arr:
            arr.append(st)
            return
    if len(st) > 7:
        return
    else:
        for i in range(4):
            if 0 <= x+di[i] < 4 and 0 <= y+dj[i] < 4:
                x += di[i]
                y += dj[i]
                f(x, y, st + a[x][y])
                x -= di[i]
                y -= dj[i]

T = int(input())
for tc in range(1, T + 1):
    a = [list(input().split()) for _ in range(4)]
    arr = []
    for i in range(4):
        for j in range(4):
            f(i, j, str(a[i][j]))
    print(f'#{tc} {len(arr)}')
