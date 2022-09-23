# from collections import deque
#
# K = deque((i*i+(i-1)*(i-1)) for i in range(1, 40))
# K.appendleft(0)
#
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     a = deque(list(map(int, input().split())) for _ in range(N))
#     mm = 0
#     ans = 0
#     for i in range(N):
#         for j in range(N):
#             for k in range(N*2-1):
#                 h = 0
#                 vis = deque([0] * N for _ in range(N))
#                 q = deque()
#                 q.append([i, j])
#                 vis[i][j] = 1
#                 while q:
#                     x, y = q.popleft()
#                     for l in range(4):
#                         if 0 <= x + di[l] < N and 0 <= y + dj[l] < N and vis[x][y] <= k:
#                             if vis[x+di[l]][y+dj[l]] == 0:
#                                 q.append([x+di[l], y+dj[l]])
#                                 vis[x+di[l]][y+dj[l]] = vis[x][y] + 1
#                     h += a[x][y]
#                 if h * M - K[k] >= mm:
#                     mm = h * M - K[k]
#                     ans = k
#     print(ans)
#
cost = [k*k + (k-1)*(k-1) for k in range(40)]

def f(si, sj):
    global ans
    q = []
    v = [[0]*N for _ in range(N)]
    cnt = 0

    q.append((si, sj))
    v[si][sj]=1
    cnt += arr[si][sj]
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0 <= nj < N and v[ni][nj]==0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] +1
                if arr[ni][nj]==1:
                    cnt+=1
                    if cost[v[ni][nj]] <= cnt * K and ans < cnt:
                        ans = cnt
def ff():
    for si in range(N):
        for sj in range(N):
            f(si, sj)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    ff()
    print(f'#{tc} {ans}')