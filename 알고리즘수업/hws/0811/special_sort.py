T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    for i in range(N-1):
        if i % 2 == 0:
            for j in range(i+1,N):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
        if i % 2 == 1:
            for j in range(i + 1,N):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
    print(f'#{tc}', end=' ')
    print(*a[0:10], sep=' ')