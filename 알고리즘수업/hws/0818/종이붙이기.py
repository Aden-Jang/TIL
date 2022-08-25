def od(n):
    if n == 1:
        return 1
    else:
        return od(n-2) * 4 + 1

def ev(n):
    if n == 2:
        return 3
    else:
        return ev(n-2) * 4 - 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if (N // 10) % 2 == 1:
        ans = od(N//10)
    else:
        ans = ev(N//10)
    print(f'#{tc} {ans}')