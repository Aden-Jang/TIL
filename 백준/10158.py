# 메모리 초과
#
# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())
# a = [[1] + [0] * (w + 1) + [1] for _ in range(h + 1)]
# a.insert(0, [1] * (w + 3))
# a.append([1] * (w + 3))
# d = [[-1, 1], [-1, -1], [1, -1], [-1, -1]]
# sj, si = p + 1, h - q + 1
# i = 0
# l = 0
#
# while i < t:
#     di, dj = d[l]
#     if a[si + di][sj + dj] == 1:
#         l = (l + 1) % 4
#     else:
#         si, sj = si + di, sj + dj
#         i += 1
#
# print(sj - 1, h - si + 1)


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
tw = t % (2 * w)
th = t % (2 * h)
d = [1, -1]
l = 0
i = 0
while i < tw:
    if p == w or p == 0:
        l = (l + 1) % 2
        p += d[l]
    else:
        p += d[l]
    i += 1

m = 0
i = 0
while i < th:
    if q == h or q == 0:
        m = (m + 1) % 2
        q += d[m]
    else:
        q += d[m]
    i += 1
print(p, q)