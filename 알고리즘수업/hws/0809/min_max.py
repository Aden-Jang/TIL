T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    maxa = a[0]
    mina = a[0]
    for i in range(N):
        if a[i] > maxa:
            maxa = a[i]
        if a[i] < mina:
            mina = a[i]
    print(f'#{tc} {maxa - mina}')