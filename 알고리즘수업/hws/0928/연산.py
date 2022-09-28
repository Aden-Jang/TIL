from collections import deque

def f(s):
    q = deque()
    q.append((s, 0))
    vis = [0] * 1000001
    vis.append(s)
    while q:
        n, cnt = q.popleft()
        if n == M:
            return cnt
        for i in range(4):
            if i == 0:
                if 1 <= n + 1 <= 1000000 and vis[n + 1] == 0:
                    q.append((n + 1, cnt + 1))
                    vis[n + 1] = 1
            elif i == 1:
                if 1 <= n - 1 <= 1000000 and vis[n - 1] == 0:
                    q.append((n - 1, cnt + 1))
                    vis[n - 1] = 1
            elif i == 2:
                if 1 <= n * 2 <= 1000000 and vis[n * 2] == 0:
                    q.append((n * 2, cnt + 1))
                    vis[n * 2] = 1
            elif i == 3:
                if 1 <= n - 10 <= 1000000 and vis[n - 10] == 0:
                    q.append((n - 10, cnt + 1))
                    vis[n - 10] = 1

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    ans = f(N)
    print(f'#{tc} {ans}')