def f(ind, num):
    global ans
    if num == int(cnt):
        ans = max(int(''.join(a)), ans)
        return
    for i in range(ind, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] <= a[j]:
                a[i], a[j] = a[j], a[i]
                f(i, num + 1)
                a[i], a[j] = a[j], a[i]

    if ans == 0 and num < int(cnt):
        extra = (int(cnt) - num) % 2
        if extra == 1:
            a[-1], a[-2] = a[-2], a[-1]
        f(ind, int(cnt))

T = int(input())
for tc in range(1, T + 1):
    a, cnt = input().split()
    a = list(a)
    ans = 0
    f(0, 0)

    print(f'#{tc} {ans}')