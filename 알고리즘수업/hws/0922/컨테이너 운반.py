# def f(i, j):
#     global sm
#     global cnt
#     if
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     wi = list(map(int, input().split()))
#     ti = list(map(int, input().split()))
#     sm = 0
#     cnt = 0
#     f(0, 0)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    wi.sort(reverse=True)
    ti.sort(reverse=False)
    sm = 0
    for i in range(N):
        for j in range(len(ti)):
            if wi[i] <= ti[j]:
                sm += wi[i]
                ti.pop(j)
                break
    print(f'#{tc} {sm}')