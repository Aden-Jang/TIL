T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    a = 0
    ans = ''
    for i in range(1, 13):
        if N > a + (2**(-i)):
            a += 2**(-i)
            ans += '1'
        elif N < a + (2**(-i)):
            ans += '0'
        else:
            a += 2 ** (-i)
            ans += '1'
            break
    if a == N:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} overflow')