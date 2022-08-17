# stack1_stack
stackSize = 10
stack = [0] * stackSize
top = -1

top += 1        # push(1) 탑 증가
stack[top] = 1  # 스택에 push

top += 1        # push(2)
stack[top] = 2

top -= 1
temp = stack[top + 1]
print(temp)

temp = stack[top]
top -= 1
print(temp)

stack2 = []
stack2.append(10)
stack2.append(20)
print(stack2.pop())
print(stack2.pop())

# stack1_재귀
def f(i, N):        # i 현재 단계, N 목표 단계
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0, 3)
# f(0, 1000) -> 재귀 호출 횟수 초과 오류 - 재귀의 횟수는 엄청 많다면(수백번) 접근방식이 틀린것

# stack1_재귀
# 크기가 N인 배열의 모든 원소에 접근하는 재귀함수
def f(i, N):
    if i == N:      # 배열을 벗어남
        return
    else:           # 남은 원소가 있는 경우
        print(A[i])
        B[i] = A[i]
        f(i+1, N)   # 다음 원소로 이동
N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)             # 0번 원소부터 N개의 원소에 접근
print(B)

# stack1_recur  -> pypy를 돌리면 가능
# def f(i, N):        # i 현재 단계, N 목표 단계
#     if i == N:
#         print(i)
#         return
#     else:
#         print(i)
#         f(i+1, N)
#
# f(0, 1000)

# stack1_facto
def f(n):       # 팩토리얼 n! 1! = 1
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

print(f(20))
for i in range(21):
    print(i, f(i))

# stack1_fibo
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(21):
    print(i, fibo(i))
# for i in range(101):  # 시간이 오래걸림
#     print(i, fibo(i))

# stack1_fibo2      # 위보다 훨씬 빠르게 함
def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1] * 101
memo[0] = 0
memo[1] = 1
for i in range(101):
    print(i, fibo(i))

# stack1_fibo_dp
def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return

table = [0] * 101
fibo_dp(100)
print(table[100])
print(table[20])

# 여러번 반복할 때는 위처럼 table을 만들고 반복을 돌리는 것이 빠름
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     print(f'#{tc} {table[N]}')

# stack1_fibo_dp2
a = 0
b = 1
n = 20
for _ in range(n-1):
    a, b = b, a + b
print(b)

# stack1_dfs1
adjList = [[1, 2],      # 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]]         # 6
def dfs(v, N):
    visited = [0] * N   # visited 생성
    stack = [0] * N     # stack 생성
    top = -1
    print(v)
    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]:    # if (v의 인접 정점 중 방문 안한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1            # push(v)
                stack[top] = v
                v = w
                print(v)
                visited[w] = 1      # v <- w (w에 방문
                break
        else:                       # w가 없으면
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while을 빠져나옴

dfs(0, 7)

# stack1_dfs_input
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
V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N
stack = [0] * N
dfs(1, N)
print()

# stack1_dfs2
def dfs(v):
    print(v)        # v 방문
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 w
            dfs(w)

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N
dfs(0)