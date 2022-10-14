def f(a, b):
    q = [a]
    vis = [-1 for _ in range(n+1)]
    vis[a] = 0
    while q:
        x = q.pop()
        for i in alst[x]:
            if vis[i] == -1:
                q.append(i)
                vis[i] = vis[x] + 1
            if i == b:
                return vis[i]
    return -1


n = int(input())
a, b = map(int, input().split())
m = int(input())
alst = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    alst[x].append(y)
    alst[y].append(x)
print(f(a, b))