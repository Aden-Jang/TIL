T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    p = [[] for _ in range(1<<N)]
    ans = 0
    for i in range(1<<N):
        for j in range(N):
            if i & (1 << j):
                p[i].append(a[j])
    for i in range(len(p)):
        s = 0
        for j in range(len(p[i])):
            s += p[i][j]
        if s == K:
            ans += 1
    print(f'#{tc} {ans}')