# 큐
N = 3
q = [0] * N
front = -1
rear = -1

rear += 1       # enqueue(10)
q[rear] = 10

rear += 1       # enqueue(20)
q[rear] = 20

rear += 1       # enqueue(30)
q[rear] = 30

# 인덱스 에러 발생
# rear += 1       # enqueue(40)
# q[rear] = 40

front += 1
print(q[front]) # dequeue()

front += 1
print(q[front]) # dequeue()

front += 1
print(q[front]) # dequeue()

# 순환 큐

N = 3
q = [0] * N
front = 0
rear = 0

rear = (rear + 1) % N       # enqueue(10)
q[rear] = 10

rear = (rear + 1) % N      # enqueue(20)
q[rear] = 20

rear = (rear + 1) % N       # enqueue(30)
q[rear] = 30

rear = (rear + 1) % N       # enqueue(30)
q[rear] = 40

# 인덱스 에러 발생
# rear += 1       # enqueue(40)
# q[rear] = 40

front = (front + 1) % N
print(q[front]) # dequeue()

front = (front + 1) % N
print(q[front]) # dequeue()

front = (front + 1) % N
print(q[front]) # dequeue()


# 큐2

q = []

q.append(10)
q.append(20)
q.append(30)

print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

# 위 방식은 백만개 쯤 하면 느려짐 아래를 사용하면 속도문제 해결 가능
from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)

print(q.popleft())
print(q.popleft())
print(q.popleft())


# 마이쮸 나눠주기

p = 1       # 처음 줄 설 사람 번호

q = []
N = 20      # 초기 마이쮸 개수
m = 0       # 나눠준 개수
v = 0

while m < N:
    q.append((p, 1, 0))     # 처음 줄 서는 사람
    # print(q)
    v, c, my = q.pop(0)
    # print(f'큐에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수 {c}, 나눠준 마이쮸 수 {m}')
    m += c
    q.append((v, c+1, my+c))     # 마이쮸를 받고 다시 서는 사람, 매번 줄 선 횟수만큼 마이쮸 배급
    p += 1
print(f'마지막 받은 사람 : {v}')

# deque사용

from collections import deque

p = 1       # 처음 줄 설 사람 번호

q = deque()
N = 1000000      # 초기 마이쮸 개수
m = 0       # 나눠준 개수
v = 0

while m < N:
    q.append((p, 1, 0))     # 처음 줄 서는 사람
    # print(q)
    v, c, my = q.popleft()
    # print(f'큐에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수 {c}, 나눠준 마이쮸 수 {m}')
    m += c
    q.append((v, c+1, my+c))     # 마이쮸를 받고 다시 서는 사람, 매번 줄 선 횟수만큼 마이쮸 배급
    p += 1
print(f'마지막 받은 사람 : {v}')


# BFS 알고리즘1 양식
def BFS(G, v):              # 그래프 G, 탐색 시작점 v
    visited = [0] * (n+1)   # n : 정점의 개수
    queue = []              # 큐 생성
    queue.append(v)         # 시작점 v를 큐에 삽입
    while queue:            # 큐가 비어있지 않은 경우
        t = queue.pop(0)    # 큐의 첫번째 원소 반환
        if not visited[t]:  # 방문되지 않은 곳이라면
            visited[t] = True # 방문한 것으로 표시
            visit(t)        # 정점 t에서 할 일
            for i in G[t]:  # t와 연결된 모든 정점에 대해
                if not visited[i]:  # 방문되지 않은 곳이라면
                    queue.append(i) # 큐에 넣기


# BFS 알고리즘2 양식
def BFS(G, v):              # 그래프 G, 탐색 시작점 v
    visited = [0] * (n+1)   # n : 정점의 개수
    queue = []              # 큐 생성
    queue.append(v)         # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue:            # 큐가 비어있지 않은 경우
        t = queue.pop(0)    # 큐의 첫번째 원소 반환
        visit(t)            # 정점 t에서 할 일
        for i in G[t]:      # t와 연결된 모든 정점에 대해
            if not visited[i]:  # 방문되지 않은 곳이라면
                queue.append(i) # 큐에 넣기
                visited[i] = visited[t] + 1 # n으로부터 1만큼


# BFS1
'''
adjList = [[1, 2],      # 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]]         # 6
'''
def bfs(v, N):                  # v 시작정점, N : 마지막 정점
    visited = [0] * (N+1)       # visited 생성
    q = []                      # 큐 생성
    q.append(v)                 # 시작점 enqueue
    visited[v] = 1              # 시작점 처리 표시
    while q:                    # 큐가 비어있지 않으면
        v = q.pop(0)            # dequeue
        print(v)                # visit(v)
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

V, E = map(int, input().split())
N = V + 1                       # N 정점 개수
adjList = [[] for _ in range(N)]
'''
0번부터 N번까지 E개의 간선
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
bfs(0, V)


# BFS2

def bfs(v, N, t):               # v : 시작, N : 마지막 정점번호, t : 찾는 정점
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:              # visit(v)
            return visited[99]            # 목표 발견
        for w in adjList[v]:    # v에 인접하고 방문 안한 w enqueue, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0
T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        adjList[a].append(b)

    print(f'#{tc} {bfs(0, 99, 99)}')      # 시작, 마지막 정점, 목표 정점 번호


# queue_4875미로
'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:         # 3번인가??
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:         # '2'
                sti, stj = i, j
                break
        if sti != -1:
            break

    print(f'#{tc} {bfs(sti, stj, N)}')

# 미로 최단거리 dfs
'''
3
5
11111
12001
10101
13001
11111
5
11111
12131
10111
10001
11111
9
111111111
120000001
101110101
100000101
111110101
101000101
101011101
100000031
111111111
'''


def dfs(i, j, N):
    global answer
    if maze[i][j] == 3:
        answer += 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:      # 벽으로 둘러쌓인 미로여서 인덱스 걱정 안해도됨
                dfs(ni, nj, N)
        visited[i][j] = 0
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # '2'
                sti, stj = i, j
                break
        if sti != -1:
            break
    answer = 0      # 경로의 수
    visited = [[0] * N for _ in range(N)]
    dfs(sti, stj, N)
    print(answer)
    # print(f'#{tc} {dfs(sti, stj, N)}')

# 미로 최단거리 dfs2
'''
3
5
11111
12001
10101
13001
11111
5
11111
12131
10111
10001
11111
9
111111111
120000001
101110101
100000101
111110101
101000101
101011101
100000031
111111111
'''


def dfs(i, j, s, N):
    global minV
    if maze[i][j] == 3:
        if minV > s + 1:
            minV = s + 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:      # 벽으로 둘러쌓인 미로여서 인덱스 걱정 안해도됨
                dfs(ni, nj, s+1, N)
        visited[i][j] = 0
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # '2'
                sti, stj = i, j
                break
        if sti != -1:
            break
    answer = 0      # 경로의 수
    minV = N * N
    visited = [[0] * N for _ in range(N)]
    dfs(sti, stj, 0, N)
    if minV == N * N:
        minV = -1
    print(f'#{tc} {minV}')

# bfs 3
'''
3
5
11111
12001
10101
12001
11111
5
11111
12121
10111
10001
11111
9
111111111
120000001
101110101
100002101
111110101
121000101
101011101
100000021
111111111
'''

def bfs(N):
    visited = [[0]*N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i,j))
                visited[i][j] = 1
    while q:
        i, j = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs(N)}')

