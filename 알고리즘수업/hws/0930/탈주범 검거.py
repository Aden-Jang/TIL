dic = {1 : ((1, 0), (-1, 0), (0, 1), (0, -1)), 2 : ((1, 0), (-1, 0)), 3 : ((0, 1), (0, -1)),
       4 : ((1, 0), (0, 1)), 5 : ((-1, 0), (0, 1)), 6 : ((-1, 0), (0, -1)), 7: ((1, 0), (0, -1))}


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    vis = [[0] * M for _ in range(N)]
    vis[R][C] = 1
    q = []
    q.append((R, C))
    ans = 0
    # x, y = q.pop(0)
    # print(dic[x+dic[a[x][y]][i][0]][y+dic[a[x][y]][i][1]])
    #
    # print(x, y)
    while q:
        x, y = q.pop(0)
        if a[x][y] != 0:
            for i in range(len(dic[a[x][y]])):
                # print(-(dic[a[x][y]][i][0]), -(dic[a[x][y]][i][1]))
                # print([a[x+dic[a[x][y]][i][0]][y+dic[a[x][y]][i][1]]])
                if 0 <= x+dic[a[x][y]][i][0] < N and 0 <= y+dic[a[x][y]][i][1] < M:
                    if vis[x+dic[a[x][y]][i][0]][y+dic[a[x][y]][i][1]] == 0 and a[x+dic[a[x][y]][i][0]][y+dic[a[x][y]][i][1]] != 0 and (-(dic[a[x][y]][i][0]), -(dic[a[x][y]][i][1])) in dic[a[x+dic[a[x][y]][i][0]][y+dic[a[x][y]][i][1]]]:
                        vis[x+dic[a[x][y]][i][0]][y+dic[a[x][y]][i][1]] = vis[x][y] + 1
                        q.append((x+dic[a[x][y]][i][0], y+dic[a[x][y]][i][1]))
    for i in range(N):
        for j in range(M):
            if 0 < vis[i][j] <= L:
                ans += 1
    print(*vis, sep='\n')
    print(f'#{tc} {ans}')