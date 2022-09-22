from collections import deque
N, K = map(int, input().split())
a = deque(range(1, N + 1))
ans = []
while a:
    for i in range(K):
        if i == K-1:
            ans.append(a.popleft())
        else:
            a.append(a.popleft())

print('<', end='')
print(*ans, sep=', ', end='')
print('>')