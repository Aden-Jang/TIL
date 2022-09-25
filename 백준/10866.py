from collections import deque
q = deque()
N = int(input())
a = [list(input().split()) for _ in range(N)]

for i in range(N):
    if a[i][0] == 'push_front':
        q.appendleft(a[i][1])
    elif a[i][0] == 'push_back':
        q.append(a[i][1])
    elif a[i][0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a[i][0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif a[i][0] == 'size':
        print(len(q))
    elif a[i][0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif a[i][0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif a[i][0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)