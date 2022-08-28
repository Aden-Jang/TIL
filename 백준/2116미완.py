def idx(x):
    if x == 0:
        return 5
    elif x == 1:
        return 3
    elif x == 2:
        return 4
    elif x == 3:
        return 1
    elif x == 4:
        return 2
    elif x == 5:
        return 0


N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(6):
    for j in range(N):
        m = [4, 5, 6]
        nid = idx(i)