N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
a.sort()

r , l = max(a)[0], min(a)[0]
h = max(a, key=lambda x: x[1])
maxidx = a.index(h)
ans = h[1]
sh = a[0][1]
eh = a[-1][1]

for i in range(0, maxidx):
    if a[i][1] >= sh:
        sh = a[i][1]
    ans += (a[i+1][0] - a[i][0]) * sh

for i in range(N-1, maxidx, -1):
    if a[i][1] >= eh:
        eh = a[i][1]
    ans += (a[i][0] - a[i-1][0]) * eh
print(ans)