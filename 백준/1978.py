N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    if i == 2:
        ans += 1
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i-1:
            ans += 1
print(ans)