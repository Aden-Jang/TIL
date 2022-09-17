N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
a1 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
a2 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
minn = 64
for i in range(N-7):
    for j in range(M-7):
        m1 = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 1:
                    if a1[l] != a[i+k][j+l]:
                        m1 += 1
                else:
                    if a1[l] == a[i+k][j+l]:
                        m1 += 1
        minn = min(minn, m1, 64-m1)
print(minn)
