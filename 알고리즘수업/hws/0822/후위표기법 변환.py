T = int(input())
for tc in range(1, T+1):
    a = list(input())
    si = []
    for i in range(len(a)):
        if a[i] == '*':
            si.append(i)
    for i in range(len(a)):
        if i in si:
            a[i], a[i+1] = a[i+1], a[i]
    for i in range(len(a)):
        if a[i] == '+':
            p = a.pop(i)
            a.append(p)
            break
    print(f'#{tc}', end=' ')
    print(*a, sep='')