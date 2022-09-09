a = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))
ans = []
for i in range(6):
    b = a[i] - chess[i]
    ans.append(b)
print(*ans)