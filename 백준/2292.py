N = int(input())
i = 1
N -= 1
ans = 1
while N >= 1:
    N = N - 6*i
    i += 1
    ans += 1
print(ans)