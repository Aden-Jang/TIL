def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(n**(1/2) + 1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i * j] = False
                j += 1

    return arr

M, N = map(int, input().split())
arr = is_prime_num(N)
for i in range(M, N+1):
    if arr[i] == True:
        print(i, end=' ')