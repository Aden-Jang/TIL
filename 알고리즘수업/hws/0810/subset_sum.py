T = int(input())
for tc in range(1,T+1):
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1<<10):
        sa = 0
        for j in range(10):
            if i == 0 and j == 0:
                sa = 1
            if i & (1<<j):
                sa += a[j]
        if sa == 0:
            ans = 1
            break
    print(f'#{tc} {ans}')