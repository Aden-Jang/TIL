def f(i, k):
    global ans
    if i == k:
        aa = []
        for j in range(k):
            if bit[j]:
                aa.append(arr[j])
        if len(aa) == N:
            if sum(aa) == K:
                ans += 1
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(range(1,13))
    n = len(arr)
    aaa = []
    bit = [0] * n
    ans = 0
    f(0, n)
    print(f'#{tc} {ans}')