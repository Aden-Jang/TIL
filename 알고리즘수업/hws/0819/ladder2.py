for _ in range(10):
    tc = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if a[0][i] == 1:
            x = i
            j = 0
            mov = 0
            while j < 99:
                j += 1
                if i == 0:
                    if a[j][i + 1] == 1:
                        while a[j][i + 1] == 1:
                            i += 1
                            mov += 1
                elif i == 99:
                    if a[j][i - 1] == 1:
                        while a[j][i - 1] == 1:
                            i -= 1
                            mov += 1
                else:
                    if a[j][i + 1] == 1:
                        while a[j][i + 1] == 1:
                            i += 1
                            mov += 1
                            if i == 99:
                                break
                    elif a[j][i - 1] == 1:
                        while a[j][i - 1] == 1:
                            i -= 1
                            mov += 1
                            if i == 0:
                                break
            if x == 0:
                minm = mov
                ans = x
            else:
                if mov < minm:
                    minm = mov
                    ans = x
    print(f'#{tc} {ans}')