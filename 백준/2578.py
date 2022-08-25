a = [list(map(int, input().split())) for _ in range(5)]
s = [list(map(int, input().split())) for _ in range(5)]
sa = []
ans = [[0]*5 for _ in range(5)]


for i in range(5):
    for j in range(5):
        sa.append(s[i][j])
ansnum = 0
for i in sa:
    for j in range(5):
        for k in range(5):
            if a[j][k] == i:
                ans[j][k] = 1
                ansnum = 0
                for l in range(5):
                    if ans[l] == [1, 1, 1, 1, 1]:
                        ansnum += 1
                for l in range(5):
                    if ans[l][l] == 0:
                        break
                    if l == 4:
                        ansnum += 1
                for l in range(5):
                    if ans[l][4-l] == 0:
                        break
                    if l == 4:
                        ansnum += 1
                aw = list(zip(*ans))
                for l in range(5):
                    if aw[l] == (1, 1, 1, 1, 1):
                        ansnum += 1
                if ansnum >= 3:
                    break
            if ansnum >= 3:
                break
        if ansnum >= 3:
            break
    if ansnum >= 3:
        break
print(sa.index(i)+1)
