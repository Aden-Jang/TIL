for tc in range(1, 11):
    N = int(input())
    a = [list(str(input())) for _ in range(100)] # 문자열을 리스트로 받아옴
    ans = 1
    for k in range(100):
        for i in range(100):
            for j in range(99, i, -1):
                x = i
                y = j
                if a[k][x] == a[k][y]:
                    num = j - i + 1
                    while True:
                        y -= 1
                        x += 1
                        if y - x <= 1 and a[k][x] == a[k][y]:
                            if num > ans:
                                ans = num
                            break
                        elif a[k][x] == a[k][y]:
                            continue
                        else:
                            break
    for i in range(100): # 전치시킴
        for j in range(100):
            if i < j:
                a[i][j], a[j][i] = a[j][i], a[i][j]
    for k in range(100):
        for i in range(100):
            for j in range(99, i, -1):
                x = i
                y = j
                if a[k][x] == a[k][y]:
                    num = j - i + 1
                    while True:
                        y -= 1
                        x += 1
                        if y - x <= 1 and a[k][x] == a[k][y]:
                            if num > ans:
                                ans = num
                            break
                        elif a[k][x] == a[k][y]:
                            continue
                        else:
                            break

    print(f'#{tc} {ans}')
