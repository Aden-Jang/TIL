T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, (input().split()))
    t = [0] * (N + 1)
    for _ in range(M):
        ln, num = map(int, input().split())
        t[ln] = num
    for i in range(N, 0, -1):
        if t[i] != 0:
            continue
        else:
            if 2*i+1 > N:
                t[i] = t[2*i]
            else:
                t[i] = t[2*i] + t[2*i+1]
    print(f'#{tc} {t[L]}')
