def preo(N):
    global cnt
    if N:
        preo(ch1[N])
        cnt += 1
        preo(ch2[N])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1
    a = list(map(int, input().split()))
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(E):
        if ch1[a[i * 2]] == 0:
            ch1[a[i * 2]] = a[i * 2 + 1]
        else:
            ch2[a[i * 2]] = a[i * 2 + 1]
    cnt = 0
    preo(N)
    print(f'#{tc} {cnt}')
