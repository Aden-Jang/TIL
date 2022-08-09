T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(N-M+1):
        mm = 0
        for j in range(i,i+M):
            mm += a[j]
        if i == 0:
            mina = mm
            maxa = mm
        if mm >= maxa:
            maxa = mm
        if mm <= mina:
            mina = mm
    print(f'#{tc} {maxa-mina}')


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    a = list(map(int,input().split()))
    sm = 0
    for i in range(M):
        sm += i
    maxa = mina = sm
    for i in range(M, N):
        sm += a[i]
        sm -= a[i - M]
        if sm >= maxa:
            maxa = sm
        if sm <= mina:
            mina = sm
    print(f'#{tc} {maxa - mina}')