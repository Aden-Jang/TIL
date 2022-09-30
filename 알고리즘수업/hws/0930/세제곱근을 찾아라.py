T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = -1
    s, e = 1, N
    while s <= e:
        m = (s + e) // 2
        if m ** 3 == N:
            ans = m
            break
        elif m ** 3 < N:
            s = m + 1
        else:
            e = m - 1

    print(f'#{test_case} {ans}')