import sys
from collections import deque

sys.stdin = open("input.txt", "r")


N, M = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]
dx = [ 0, 0, 1, -1 ]
dy = [ 1, -1, 0, 0 ]

dq = deque()
cnt = sum(map(sum, cheese))
time = 0
visited = [[0]*M for _ in range(N)]
dq.append((0, 0))
visited[0][0] = 1

def BFS():
    global dq
    nq = deque()
    while dq:
        y, x =  dq.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if not 0 <= ny < N and not 0 <= nx < M:
                continue
            if cheese[ny][nx] == 0 and visited[ny][nx] == 0:
                dq.append((ny, nx))
                visited[ny][nx] = 1

            if cheese[ny][nx] == 1 and visited[ny][nx] == 0:
                nq.append((ny, nx))
                visited[ny][nx] = 1

    return nq
nl= [cnt]
while dq:
    dq = BFS()
    time += 1
    cnt -= len(dq)
    nl.append(cnt)

time -= 1
print(time)
print(nl[time-1])









