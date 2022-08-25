for _ in range(1, 11):
    tc, n = map(int, input().split())
    a = list(map(int, input().split()))
    lst1 = [[] for _ in range(100)]
    for i in range(len(a)):
        if i % 2 == 0:
            lst1[a[i]].append(a[i+1])
    ans = 0
    vis = [0] * 100
    stk = [0] * 100
    s = 0
    top = -1
    vis[s] = 1
    while True:
        if s == 99:
            ans = 1
            break
        for i in lst1[s]:
            if i == 0:
                continue
            elif vis[i] == 0:
                top += 1
                stk[top] = s
                s = i
                vis[i] = 1
                break
        else:
            if top != -1:
                s = stk[top]
                top -= 1
            else:
                break
    print(f'#{tc} {ans}')