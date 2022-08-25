K = int(input())
a = [list(map(int, input().split())) for _ in range(6)]

if a[0][0] == a[4][0]:
    if a[1][0] == a[5][0]:
        sb = a[0][1] * a[5][1]
        i = 4
    else:
        sb = a[5][1] * a[4][1]
        i = 4
else:
    i = 0
    while i < 3:
        if i == 0:
            if a[i][0] == a[i+2][0]:
                if a[i+1][0] == a[i+3][0]:
                    sb = a[i+1][1] * a[i+2][1]
                else:
                    sb = a[i][1] * a[i+1][1]
                break
        if a[i][0] == a[i+2][0]:
            if a[i+1][0] == a[i+3][0]:
                sb = a[i+1][1] * a[i+2][1]
                break
        i += 1
bb = 1
for j in range(6):
    if a[j][0] not in [a[i][0], a[i+1][0]]:
        bb *= a[j][1]
ans = bb - sb
print(ans * K)