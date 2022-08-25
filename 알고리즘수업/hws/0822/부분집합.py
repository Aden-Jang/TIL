# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     a = list(map(int, input().split()))
#     p = [[] for _ in range(1<<N)]
#     ans = 0
#     for i in range(1<<N):
#         for j in range(N):
#             if i & (1 << j):
#                 p[i].append(a[j])
#     for i in range(len(p)):
#         s = 0
#         for j in range(len(p[i])):
#             s += p[i][j]
#         if s == K:
#             ans += 1
#     print(f'#{tc} {ans}')


def dfs(n, sm):
    global ans

    # 가지치기는 제일 위에서, 제일 마지막 순서로
    if sm > K: # 이미 K값 초과해서 답을 찾을 가능성이 없는 경우
        return

    # 종료조건
    if n == N:
        if sm == K:
            ans += 1
        return

    # dfs(n+1) 호출
    # 해당 원소를 사용하는 경우
    dfs(n+1, sm + a[n])
    # 해당 원소를 사용하지 않는 경우
    dfs(n+1, sm)



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    dfs(0, 0)

    print(f'#{tc} {ans}')