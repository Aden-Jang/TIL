T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    a.sort(key=lambda x: (x[1], -x[0]))
    st = 0
    et = 0
    cnt = 0
    for s, e in a:
        if s >= et:
            st = s
            et = e
            cnt += 1
    print(f'#{tc} {cnt}')
