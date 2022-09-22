N = int(input())
a = [list(input().split()) for _ in range(N)]
for i in range(1, N + 1):
    a[i-1].append(i)
    a[i-1][0] = int(a[i-1][0])
a.sort(key=lambda x:(x[0], x[2]))
for i in range(N):
    print(a[i][0], a[i][1])