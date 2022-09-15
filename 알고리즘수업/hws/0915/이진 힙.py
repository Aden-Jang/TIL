T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    # for _ in range(20):
    #     for i in range(1, N + 1):
    #         if 2*i == N:
    #             a[i], a[i*2] = min(a[i*2], a[i]), max(a[i*2], a[i])
    #         elif 2*i+1 <= N:
    #             if a[i*2] <= a[i*2+1]:
    #                 a[i], a[i*2] = min(a[i*2], a[i]), max(a[i*2], a[i])
    #             else:
    #                 a[i], a[i*2+1] = min(a[i*2+1], a[i]), max(a[i*2+1], a[i])
    #         else:
    #             continue
    # ans = 0
    # while N > 0:
    #     N //= 2
    #     ans += a[N]
    k = []
    for i in range(len(a)):
        k.append(a[i])
        while i//2 != 0:
            if a[i] < a[i//2]:
                a[i], a[i//2] = a[i//2], a[i]
            i = i//2
    ans = 0
    while N > 0:
        N //= 2
        ans += a[N]
    print(f'#{tc} {ans}')