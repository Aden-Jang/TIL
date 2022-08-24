for _ in range(10):
    tc = int(input())
    a = list(map(int, input().split()))
    i = 1
    while a[-1] > 0:
        z = a.pop(0)
        z -= i
        i += 1
        if i == 6:
            i = 1
        if z <= 0:
            z = 0
        a.append(z)

    print(f'#{tc} ', end = '')
    print(*a)