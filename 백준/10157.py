C, R = map(int, input().split())
K = int(input())
a = [[1] + [0] * C + [1] for _ in range(R)]
a.insert(0, [1] * (C+2))
a.append([1] * (C+2))
si, sj = R, 1
i = 1
x = 0
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
if K > C * R:
    ans = 0
    print(ans)
else:
    while i <= K:
        a[si][sj] = i
        if i == K:
            break
        di, dj = d[x]
        if a[si+di][sj+dj] == 0:
            si, sj = si + di, sj + dj
            i += 1
        else:
            x = (x + 1) % 4
    print(sj, R - si + 1)
for l in a:
    print(l)
