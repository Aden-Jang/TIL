def f():


T = int(input())
for tc in range(1, T + 1):
    a = list(map(int, input().split()))
    N = a.pop(0)
    vis = [0] * N
    ans = 100 * N
    # cnt = 0
    # i = 0
    # b = a[0]
    #
    # while i < N:
    #     if i + b >= N-1:
    #         break
    #     else:
    #         a1 = a[i+1:i+b+1]
    #         b = max(a1)
    #         mj = a1[0]
    #         mji = 0
    #         for j in range(len(a1)):
    #             if mj <= a1[j] and b < a1[j]+j+1:
    #                 mji = j
    #         i += j + 1
    #         cnt += 1
    # print(f'#{tc} {cnt}')

