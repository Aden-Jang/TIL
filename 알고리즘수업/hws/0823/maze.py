T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    a.insert(0, [1] * (N+2))
    a.append([1] * (N+2))
    stk = []
    for i in range(N+2):
        for j in range(N+2):
            if a[i][j] == 2:
                stk.append((i, j))
    i, j = stk[0]
    a[i][j] = 0
    ans = 0
    while True:
        if a[i-1][j] == 3 or a[i+1][j] == 3 or a[i][j-1] == 3 or a[i][j+1] == 3:
            ans = 1
            break
        if a[i-1][j] == 0 and (i-1, j) not in stk:
            i -= 1
            stk.append((i, j))
            continue
        elif a[i+1][j] == 0 and (i+1, j) not in stk:
            i += 1
            stk.append((i, j))
            continue
        elif a[i][j-1] == 0 and (i, j-1) not in stk:
            j -= 1
            stk.append((i, j))
            continue
        elif a[i][j+1] == 0 and (i, j+1) not in stk:
            j += 1
            stk.append((i, j))
            continue
        a[i][j] = 1

        if a[i-1][j] == 0:
            a[i][j] = 1
            i -= 1
            stk.pop()
            continue
        elif a[i+1][j] == 0:
            a[i][j] = 1
            i += 1
            stk.pop()
            continue
        elif a[i][j-1] == 0:
            a[i][j] = 1
            j -= 1
            stk.pop()
            continue
        elif a[i][j+1] == 0:
            a[i][j] = 1
            j += 1
            stk.pop()
            continue
        break
    print(f'#{tc} {ans}')
