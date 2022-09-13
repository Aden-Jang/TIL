def pre(n):
    if n:
        print(n, end=' ')
        pre(ch1[n])
        pre(ch2[n])

T = int(input())
for tc in range(1, T+1):
    V = int(input())
    a = list(map(int, input().split()))
    root = 1
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    for i in range(V-1):
        p, c = a[i*2], a[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    print(f'#{tc}', end=' ')
    pre(root)
    print()