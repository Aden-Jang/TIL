T = int(input())
for tc in range(1, T+1):
    a = [input().split() for _ in range(5)]
    mlen = 0
    for i in range(5):
        if len(a[i]) > mlen:
            mlen = len(a[i])

    print(f'#{tc}',end = ' ')
    for j in range(mlen):
        for i in range(5):
            if j <= len(a[i]):
                print(a[i][j], end = '')
    print()