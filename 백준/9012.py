from collections import deque
T = int(input())
for _ in range(T):
    q = deque()
    a = input()
    ans = 'YES'
    for i in a:
        if i == '(':
            q.append(i)
        elif i == ')':
            if q:
                q.pop()
            else:
                ans = 'NO'
                break
    if q:
        ans = 'NO'
    print(ans)