T = int(input())
for tc in range(1,T+1):
    N, D = map(int,input().split())
    a = list(map(int,input().split()))
    l = 0
    r = N-1
    c = (r+l)//2
    while 1:
        if a[c] == D:
            ans = c + 1
            break
        elif a[c+1] == D:
            ans = c+2
            break
        elif a[c] < D:
            l = c
        elif a[c] > D:
            r = c
        c = (r+l)//2
        if r-l <= 1 and a[r] != D and a[l] != D:
            ans = 0
            break
    print(f'#{tc} {ans}')