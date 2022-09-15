N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
ans = [1] * N
for i in range(N):
    for j in range(N):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            ans[i] += 1
print(*ans)