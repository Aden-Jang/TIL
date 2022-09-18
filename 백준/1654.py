K, N = map(int, input().split())
a = [int(input()) for _ in range(K)]
mx = sum(a) // N
ans = 0
while ans < N:
    ans = 0
    for i in a:
        ans += i // mx
    if ans >= N:
        break
    mx -= 1
print(mx)