for tc in range(1,11):
    N = int(input())
    a = list(map(int,input().split()))

    for i in range(N+1):
        maxa = a[0]
        mina = a[0]
        for j in range(len(a)):
            if a[j] > maxa:
                maxa = a[j]
            if a[j] < mina:
                mina = a[j]
        a[a.index(maxa)] -= 1
        a[a.index(mina)] += 1
        if i == N:
            break
        maxa -= 1
        mina += 1
    print(f'#{tc} {maxa-mina}')