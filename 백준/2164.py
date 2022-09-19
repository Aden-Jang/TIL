from collections import deque
N = int(input())

if N <= 2:
    a = [N]
else:
    a = deque(range(N, 0, -1))

while len(a) > 1:
    a.pop()
    x = a.pop()
    a.insert(0, x)
print(a[0])