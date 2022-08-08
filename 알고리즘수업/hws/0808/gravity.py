T = int(input())
for tc in range(T):
    N = int(input())
    li = list(map(int,input().split()))
    a = 0
    for i in range(N):
        g = N-1-i
        for j in range(i+1,N):
            if li[i] <= li[j]:
                g -= 1
        a.append(g)
    print(f'#{tc+1} {max(a)}')
