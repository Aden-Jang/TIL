# def fibo(n):
#     global zn
#     global on
#     if n == 0:
#         zn += 1
#         return 0
#     elif n == 1:
#         on += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     zn = on = 0
#     fibo(N)
#     print(zn, on)

T = int(input())
for _ in range(T):
    zero = [1, 0]
    one = [0, 1]

    N = int(input())
    if N > 1:
        for i in range(N-1):
            if i % 2 == 1:
                one[0] += zero[0]
                one[1] += zero[1]
            else:
                zero[0] += one[0]
                zero[1] += one[1]
    if N % 2 == 1:
        print(*one, sep=' ')
    else:
        print(*zero, sep=' ')
