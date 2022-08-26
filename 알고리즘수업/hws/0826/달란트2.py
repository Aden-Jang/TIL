T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    a = N//P
    lst = []
    ans = 1
    for _ in range(P):
        lst.append(a)
        N -= a
    for i in range(N):
        lst[i] += 1
    for i in lst:
        ans *= i
    print(f'#{tc} {ans}')