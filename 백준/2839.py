N = int(input())
if N in [1, 2, 4, 7]:
    ans = -1
else:
    ans = N//5
    N %= 5
    while N % 3 != 0:
        N += 5
        ans -= 1
    ans += N//3
print(ans)