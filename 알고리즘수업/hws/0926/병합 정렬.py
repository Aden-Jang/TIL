def f(a, N):
    global ans
    global arr
    if len(a) == 1:
        return
    elif len(a) == 2:
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]
            ans += 1
            print(a)
            return
        else:
            return
    else:
        a1 = a[0:N//2]
        a2 = a[N//2:N]

        # print(a)
        f(a1, len(a1))
        print(f'aa{a}a')
        arr.append(a1)
        f(a2, len(a2))
        arr.append(a2)
        print(arr)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))

    arr = []
    ans = 0
    f(a, N)

    print(a)
    print(f'#{tc} {a[N//2]} {ans}')