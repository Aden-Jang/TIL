T = int(input())
for i in range(T):
    TC = int(input())
    a = list(map(int,input().split()))
    b = [0] * 101
    for j in a:
        b[100 - j] += 1
    print(f'#{TC} {100 - b.index(max(b))}')