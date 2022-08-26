T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    a = list(map(int, input().split()))
    lst = [0] * 11112
    ans = 'Possible'
    j = -K
    for i in range(0, 11112):
        if i % M == 0:
            j = j+K
        if i in a:
            j -= 1
        lst[i] = j
    for i in a:
        if lst[i] < 0:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')
