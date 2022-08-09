T = int(input())
for tc in range(1, T+1):
    N, Q = map(int,input().split())
    a = [0] * N
    for i in range(Q):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            a[j] = L
    print(f'#{tc} ',end='')
    print(*a, sep=' ')