for tc in range(1, 11):
    N, sn = map(int, input().split())
    vis = [0] * 101
    arr = [[] for _ in range(101)]
    a = list(map(int, input().split()))
    for i in range(0, N, 2):
        arr[a[i]].append(a[i+1])
    q = []
    q.append(sn)
    vis[sn] = 1
    while q:
        sn = q.pop(0)
        for i in arr[sn]:
            if vis[i] == 0:
                q.append(i)
                vis[i] = vis[sn]+1
    ans = vis[0]
    for i in range(len(vis)):
        if vis[ans] <= vis[i]:
            ans = i
    print(f'#{tc} {ans}')