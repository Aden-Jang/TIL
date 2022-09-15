N, M = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(N - 2):
    for j in range(i+1, N - 1):
        for k in range(j+1, N):
            if a[i] + a[j] + a[k] <= M:
                if ans <= a[i] + a[j] + a[k]:
                    ans = a[i] + a[j] + a[k]
print(ans)