def f(z):
    q = []
    q.append(z)
    vis = [0 for _ in range(n+2)]
    vis[z] = 1
    while q:
        x = q.pop()
        for i in alst[x]:
            if vis[i] == 0:
                if i == n+1:
                    return "happy"
                q.append(i)
                vis[i] = 1
    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    cs = []
    for i in range(n+2):
        a, b = map(int, input().split())
        cs.append((a, b, i))
    nod = []
    for i in range(n+1):
        for j in range(i+1, n+2):
            if abs(cs[i][0]-cs[j][0]) + abs(cs[i][1]-cs[j][1]) <= 50*20:
                nod.append((cs[i][2], cs[j][2]))
    alst = [[] for _ in range(n+2)]
    for i in nod:
        a, b = i
        alst[a].append(b)
        alst[b].append(a)
    print(f(0))
