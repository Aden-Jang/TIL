T = int(input())
for tc in range(1,T+1):
    a = list(range(1,13))
    ans = 0
    N,K = map(int,input().split())
    aaa = [[] for _ in range(2**12)]
    cnt = 0
    for i in range(1<<12):
        for j in range(12):
            if i & (1<<j):
                aaa[cnt].append(j+1)
        cnt += 1
    for i in range(2**12):
        suma = 0
        if len(aaa[i]) == N:
            for j in range(N):
                suma += aaa[i][j]
            if suma == K:
                ans += 1
    print(f'#{tc} {ans}')
