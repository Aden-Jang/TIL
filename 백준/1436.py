def f(N):
    a = N
    while a > 100:
        if a % 1000 == 666:
            return N
        else:
            a //= 10
    return False
N = int(input())
cnt = 0
num = 666
while cnt < N:
    ans = f(num)
    if ans:
        cnt += 1
    num += 1
print(ans)

