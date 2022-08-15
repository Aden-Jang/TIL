T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    if N in M:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')