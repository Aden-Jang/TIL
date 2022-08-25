N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
lst = [[0]*100 for _ in range(100)]
for i in range(len(a)):
    for j in range(10):
        for k in range(10):
            lst[a[i][0]+j][a[i][1]+k] = 1
ans = 0
for i in range(100):
    ans += sum(lst[i])
print(ans)