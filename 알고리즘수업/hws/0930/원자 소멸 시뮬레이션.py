d = ((0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(4001):
        for j in range(len(a)):
            if a[j][2] != 5:
                a[j][0] += d[a[j][2]][0]
                a[j][1] += d[a[j][2]][1]
        for j in range(len(a)):
            for k in range(j + 1, len(a)):
                if a[j][0:2] == a[k][0:2] and a[j][2] != 5 and a[k][2] != 5:
                    a[j][2] = a[k][2] = 4
        for j in range(len(a)):
            if a[j][2] == 4:
                ans += a[j][3]
                a[j][3] = 0
                a[j][2] = 5
        for j in range(len(a)-1, -1, -1):
            if a[j][2] == 5:
                a.pop(j)
        if len(a) <= 1:
            break
    print(f'#{tc} {ans}')