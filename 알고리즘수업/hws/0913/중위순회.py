def ino(n):
    if n:
        ino(ch1[n])
        print(di[n], end='')
        ino(ch2[n])

for tc in range(1, 11):
    V = int(input())
    a = [list(input().split()) for _ in range(V)]
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    root = 1
    di = dict()
    for i in range(V):
        di[int(a[i][0])] = a[i][1]
    for i in range(V):
        if len(a[i]) > 2:
            ch1[i+1] = int(a[i][2])
            if len(a[i]) > 3:
                ch2[i+1] = int(a[i][3])
    print(f'#{tc}', end=' ')
    ino(root)
    print()