T = int(input())
for tc in range(1, T + 1):
    a = [list(map(int,input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        lsudo = []
        rsudo = []
        for j in range(9):
            if a[i][j] not in lsudo and a[j][i] not in rsudo:
                lsudo.append(a[i][j])
                rsudo.append(a[j][i])
            else:
                ans = 0
                break
        if ans == 0:
            break

    for i in range(0,9,3):
        for j in range(0,9,3):
            ssudo = []
            for k in range(3):
                for l in range(3):
                    if a[i+k][j+l] not in ssudo:
                        ssudo.append(a[k+i][j+l])
                    else:
                        ans = 0
                        break
        if ans == 0:
            break

    print(f'#{tc} {ans}')