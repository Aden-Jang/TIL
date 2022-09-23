def f(i, sh, N ,B):
    global ans
    if i == N:
        if sh >= B and sh <= ans:
            ans = sh
        return
    if sh >= B and sh <= ans:
        ans = sh
        return
    else:
        sh += a[i]
        i += 1
        f(i, sh, N, B)
        sh -= a[i-1]
        f(i, sh, N, B)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    a = list(map(int, input().split()))
    sh = 0
    ans = 10000*N
    f(0, 0, N, B)
    print(f'#{tc} {ans-B}')