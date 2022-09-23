N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
a.sort(key=lambda x:(x[0],x[1]))
for i in range(N):
    print(a[i][0], a[i][1])