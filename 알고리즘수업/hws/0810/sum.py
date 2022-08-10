for _ in range(10):
    tc = int(input())
    a = [list(map(int,input().split())) for _ in range(100)]
    number = 0
    for i in range(100):
        number += a[0][i]
    ans = number
    for i in range(100):
        number = 0
        for j in range(100):
            number += a[i][j]
        if ans < number:
            ans = number
    for i in range(100):
        number = 0
        for j in range(100):
            number += a[j][i]
        if ans < number:
            ans = number
    number = 0
    for i in range(100):
        number += a[i][i]
        if ans < number:
            ans = number
    number = 0
    for i in range(100):
        number += a[i][99-i]
        if ans < number:
            ans = number
    print(f'#{tc} {ans}')