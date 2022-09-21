T = int(input())
for tc in range(1, T + 1):
    a = int(input())
    c = [0] * 12

    i = 0
    while i < 6:
        c[a % 10] += 1
        a //= 10
        i += 1
    tri = 0
    rrun = 0
    i = 1
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            rrun += 1
            continue
        i += 1
    if rrun + tri == 2:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')