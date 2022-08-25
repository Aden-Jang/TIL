T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    q = []
    for i in range(N):
        q.append([i+1, a[i]])
    i += 1
    while q:
        pizza = q.pop(0)
        pizza[1] //= 2
        if pizza[1] != 0:
            q.append(pizza)
        else:
            if i < M:
                q.append([i+1, a[i]])
                i += 1
    print(f'#{tc} {pizza[0]}')