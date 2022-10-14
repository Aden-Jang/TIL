def f(z):
    q = []
    vis = [0 for _ in range(N+1)]
    q.append(z)
    vis[z] = 1
    cnt = 0

    while q:
        x = q.pop()
        for i in alst[x]:
            if vis[i] == 0:
                q.append(i)
                cnt += 1
                vis[i] = 1
    return cnt

N = int(input())
s = int(input())
alst = [[] for _ in range(N+1)]
for i in range(s):
    a, b = map(int, input().split())
    alst[a].append(b)
    alst[b].append(a)
print(f(1))
