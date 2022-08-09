T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int,input().split()))
    for j in range(N-1):
        for i in range(0, N-1-j):
            if a[i] > a[i+1]:
                a[i+1], a[i] = a[i], a[i+1]
    a = ' '.join(map(str,a))
    print(f'#{tc} {a}')