T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(M):
        num = a.pop(0)
        a.append(num)
    print(f'#{tc} {a[0]}')