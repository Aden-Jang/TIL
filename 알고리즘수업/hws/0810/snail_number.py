T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    number = 1
    i = j = k = 0
    while number <= N**2:
        a[i][j] = number
        i += di[k]
        j += dj[k]
        if i<0 or i == N or j<0 or j == N or a[i][j] != 0:
            i -= di[k]
            j -= dj[k]
            k += 1
            if k == 4:
                k = 0
            if number == N**2:
                break
            number -= 1
        number += 1
    print(f'#{tc}')
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end=' ')
        print()