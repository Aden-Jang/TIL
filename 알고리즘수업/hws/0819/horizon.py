T = int(input())
for tc in range(1, T+1):
<<<<<<< HEAD
    a = [input().split() for _ in range(5)]
=======
    a = [input() for _ in range(5)]
>>>>>>> 47f883564be5cbc17670211009d0e489f2d5f8bd
    mlen = 0
    for i in range(5):
        if len(a[i]) > mlen:
            mlen = len(a[i])

    print(f'#{tc}',end = ' ')
    for j in range(mlen):
        for i in range(5):
<<<<<<< HEAD
            if j <= len(a[i]):
                print(a[i][j], end = '')
    print()
=======
            if j <= len(a[i])-1:
                print(a[i][j], end = '')
    print()
>>>>>>> 47f883564be5cbc17670211009d0e489f2d5f8bd
