def ino(n):
    global a
    if n:
        ino(ch1[n])
        a.append(n)
        ino(ch2[n])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    root = 1
    i = 2
    while i <= N:
        if i % 2 == 0:
            ch1[i//2] = i
        else:
            ch2[i//2] = i
        i += 1
    a = []
    ino(1)
    di = dict()
    for i in range(len(a)):
        di[a[i]] = i+1

    print(f'#{tc} {di[1]} {di[N//2]}')