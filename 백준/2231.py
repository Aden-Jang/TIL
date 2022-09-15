N = int(input())
if N <= 63:
    for i in range(1, N+1):
        j = i
        ans = i
        while i > 0:
            j += i % 10
            i = i//10
        if j == N:
            break
        ans = 0
else:
    for i in range(N-63, N+1):
        j = i
        ans = i
        while i > 0:
            j += i % 10
            i = i//10
        if j == N:
            break
        ans = 0
print(ans)