for tc in range(1, 11):
    N = int(input())
    a = list(input())
    si = []
    for i in range(N):
        if a[i] == '*':
            si.append(i)
    for i in range(N):
        if i in si:
            a[i], a[i + 1] = a[i + 1], a[i]
    for i in range(N):
        if a[i] == '+':
            p = a.pop(i)
            a.append(p)
            break
    stk = []
    for i in range(N):
        if a[i].isnumeric():
            stk.append(int(a[i]))
        else:
            p1 = stk.pop()
            p2 = stk.pop()
            if a[i] == '*':
                p3 = p1 * p2
            else:
                p3 = p1 + p2
            stk.append(p3)
    print(f'#{tc} {p3}')
