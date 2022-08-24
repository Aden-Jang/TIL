N = int(input())
a = list(map(int, input().split()))
ans = 1
bg = 1
sm = 1

for i in range(N-1):
    if a[i] < a[i+1]:
        bg += 1
        sm = 1
    elif a[i] > a[i+1]:
        bg = 1
        sm += 1
    else:
        bg += 1
        sm += 1
    if bg >= ans:
        ans = bg
    if sm >= ans:
        ans = sm
print(ans)