T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(input()) for _ in range(N)]
    ans = "NO"
    for i in range(N):
        for j in range(N):
            if a[i][j] == 'o':
                w = 1
                x = i
                y = j
                while y + 1 < N:
                    if a[x][y + 1] == 'o':
                        w += 1
                        y += 1
                    else:
                        break

                if w >= 5:
                    ans = 'YES'
            if a[i][j] == 'o':
                h = 1
                x = i
                y = j

                while x + 1 < N:
                    if a[x + 1][y] == 'o':
                        h += 1
                        x += 1
                    else:
                        break

                if h >= 5:
                    ans = 'YES'
            if a[i][j] == 'o':
                wh = 1
                x = i
                y = j
                while x + 1 < N and y + 1 < N:
                    if a[x + 1][y + 1] == 'o':
                        wh += 1
                        x += 1
                        y += 1
                    else:
                        break
                if wh >= 5:
                    ans = 'YES'
            if a[i][j] == 'o':
                hw = 1
                x = i
                y = j
                while x - 1 >= 0 and y + 1 < N:
                    if a[x - 1][y + 1] == 'o':
                        hw += 1
                        x -= 1
                        y += 1
                    else:
                        break
                if hw >= 5:
                    ans = 'YES'
            if ans == 'YES':
                break
        if ans == 'YES':
            break

    print(f'#{tc} {ans}')
