T = int(input())
a = [[0] * 15 for _ in range(14)]
a.append([i for i in range(15)])
for i in range(13, -1, -1):
    for j in range(1, 15):
        a[i][j] = a[i+1][j] + a[i][j-1]
for _ in range(T):
    k = int(input())
    n = int(input())
    print(a[14-k][n])