def pt(n, a):
    if n == 1:
        print(1)
        return
    if n == 2:
        pt(1, a)
        print('1 1')
    else:
        pt(n-1, a)
        for i in range(len(a)-1):
            a.append(a[i] + a[i+1])
        b = a.pop(0)
        a.append(b)
        for j in range(n - 3):
            a.pop(0)
        print(*a)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [1, 1]
    print(f'#{tc}')
    pt(N, a)