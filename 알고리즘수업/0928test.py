# # 인접
# '''
# 마지막 정점 번호(0번부터 시작), E 간선수
# 6 8
# 0 1 0 2 0 5 0 6 4 3 5 3 6 4 5 4
# '''
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
#
# adjM = [[0] * (V+1) for _ in range(V+1)]        # 인접 행렬
# adjList = [[] for _ in range(V+1)]
# for i in range(E):
#     n1, n2 = arr[i*2], arr[i*2+1]
#     adjM[n1][n2] = 1
#     adjM[n2][n1] = 1
#
#     adjList[n1].append(n2)
#     adjList[n2].append(n1)
# print(*adjM, sep='\n')
# print(adjList)

# # 상원이의 생일파티 (5521_dfs) - 틀림
# '''
# 2
# 6 5
# 2 3
# 3 4
# 4 5
# 5 6
# 2 5
# 6 5
# 1 2
# 1 3
# 3 4
# 2 3
# 4 5
# '''
#
# def dfs(i, N, c):
#     if c == 3:
#         return
#     else:
#         vis[i] = 1
#         for j in range(1, N+1):
#             if adjM[i][j] and vis[j] == 0:
#                 dfs(j, N, c+1)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     adjM = [[0]*(N+1) for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         adjM[a][b] = 1
#         adjM[b][a] = 1
#     vis = [0]*(N+1)
#
#     dfs(1, N, 0)
#     # print(f'#{tc} {sum(vis)-1}')
#     print(*adjM, sep='\n')
#     print(vis)

# 상원이의 생일파티 (5521_bfs)
def bfs(N):
    q = []              # 큐 생성
    vis = [0]*(N+1)     # vis 생성
    q.append(1)         # 시작점 인큐
    vis[1] = 1          # 시작점 방문 표시
    while q:            # 큐가 비어있지 않으면
        t = q.pop(0)
        if vis[t] > 3:
            break
        for i in range(1, N+1):
            if adj[t][i] == 1 and vis[i] == 0:
                q.append(i)
                vis[i] = vis[t] + 1
    cnt = 0
    for i in range(1, N+1):
        if 1 < vis[i] < 4:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    ans = bfs(N)

    print(f'#{tc} {ans}')
