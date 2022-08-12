T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * 200
    ans = 0

    for i in range(N):
        if a[i][0] > a[i][1]:
            a[i][0], a[i][1] = a[i][1], a[i][0]
        for j in range((a[i][0]-1)//2, (a[i][1]-1)//2+1):
            cnt[j] += 1
    for n in cnt:
        if ans < n:
            ans = n

    print(f'#{tc} {ans}')
