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
#
# # 상원이의 생일파티 (5521_bfs)
# def bfs(N):
#     q = []              # 큐 생성
#     vis = [0]*(N+1)     # vis 생성
#     q.append(1)         # 시작점 인큐
#     vis[1] = 1          # 시작점 방문 표시
#     while q:            # 큐가 비어있지 않으면
#         t = q.pop(0)
#         if vis[t] > 3:
#             break
#         for i in range(1, N+1):
#             if adj[t][i] == 1 and vis[i] == 0:
#                 q.append(i)
#                 vis[i] = vis[t] + 1
#     cnt = 0
#     for i in range(1, N+1):
#         if 1 < vis[i] < 4:
#             cnt += 1
#     return cnt
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     adj = [[0]*(N+1) for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         adj[a][b] = 1
#         adj[b][a] = 1
#     ans = bfs(N)
#
#     print(f'#{tc} {ans}')

# # mst1
# '''
# 6 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51
# '''
#
# V, E = map(int, input().split())
# adjM = [[0]*(V+1) for _ in range(V+1)]
# adjL = [[] for _ in range(V+1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjM[u][v] = w
#     adjM[v][u] = w      # 가중치가 있는 무방향 그래프
#     adjL[u].append((v, w))
#     adjL[v].append((u, w))
#
# # prim1
#
# def prim1(r, V):
#     MST = [0]*(V+1)         # MST 포함여부
#     key = [10000]*(V+1)     # 가중치의 최대값 이상으로 초기화, key[v]는 v가 MST에 속한 정점과 연결될 때 필요한 비용
#     key[r] = 0              # 시작 정점의 key
#     for _ in range(V):      # V+1개의 정점 중 V개를 선택
#         # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u찾기
#         u = 0
#         minV = 10000
#         for i in range(V+1):
#             if MST[i] == 0 and key[i] < minV:
#                 u = i
#                 minV = key[i]
#         MST[u] = 1          # 정점 u를 MST에 추가
#         # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
#         for v in range(V+1):
#             if MST[v] == 0 and adjM[u][v] > 0:
#                 key[v] = min(key[v], adjM[u][v])    # u를 통해 MST에 포함되는 비용과 기존 비용 비교
#     return sum(key)
#
#
# V, E = map(int, input().split())
# adjM = [[0]*(V+1) for _ in range(V+1)]
# adjL = [[] for _ in range(V+1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjM[u][v] = w
#     adjM[v][u] = w      # 가중치가 있는 무방향 그래프
#
# print(prim1(0, V))
#
# # prim2
#
# def prim2(r, V):
#     MST = [0]*(V+1)         # MST 포함여부
#     MST[r] = 1              # 시작정점 표시
#     s = 0                   # MST 간선의 가중치 합
#     for _ in range(V):
#         u = 0
#         minV = 10000
#         for i in range(V+1):        # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함된 정점이면
#             if MST[i] == 1:
#                 for j in range(V+1):
#                     if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
#                         u = j
#                         minV = adjM[i][j]
#         s += minV
#         MST[u] = 1
#     return s
#
# V, E = map(int, input().split())
# adjM = [[0]*(V+1) for _ in range(V+1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjM[u][v] = w
#     adjM[v][u] = w      # 가중치가 있는 무방향 그래프
#
# print(prim2(0, V))

# kruskal1

def fs(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[fs(y)] = fs(x)

V, E = map(int, input().split())        # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x:x[2])
rep = [i for i in range(V+1)]           # 대표원소 배열

N = V + 1       # 실제 정점 수
cnt = 0         # 선택한 edge의 수
total = 0       # MST 가중치의 합
for u, v, w in edge:
    if fs(u) != fs(v):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N-1:  # 간선 수
            break
print(total)