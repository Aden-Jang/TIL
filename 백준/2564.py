w, h = map(int, input().split())
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
x = list(map(int, input().split()))
lst = [0] * N
for i in range(N):
    if x[0] == a[i][0]:
        lst[i] = abs(x[1] - a[i][1])
    elif [x[0], a[i][0]] in [[1, 2], [2, 1]]:
        lst[i] = h + min(x[1] + a[i][1], 2 * w - (x[1] + a[i][1]))
    elif [x[0], a[i][0]] in [[3, 4], [4, 3]]:
        lst[i] = w + min(x[1] + a[i][1], 2 * h - (x[1] + a[i][1]))
    elif x[0] == 1:
        if a[i][0] == 3:
            lst[i] = x[1] + a[i][1]
        elif a[i][0] == 4:
            lst[i] = w - x[1] + a[i][1]
    elif x[0] == 2:
        if a[i][0] == 3:
            lst[i] = x[1] + h - a[i][1]
        elif a[i][0] == 4:
            lst[i] = w - x[1] + h - a[i][1]
    elif x[0] == 3:
        if a[i][0] == 1:
            lst[i] = x[1] + a[i][1]
        elif a[i][0] == 2:
            lst[i] = h - x[1] + a[i][1]
    elif x[0] == 4:
        if a[i][0] == 1:
            lst[i] = x[1] + w - a[i][1]
        elif a[i][0] == 2:
            lst[i] = h - x[1] + w - a[i][1]
print(sum(lst))