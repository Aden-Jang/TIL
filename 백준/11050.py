N, K = map(int, input().split())
ans = 1
for i in range(1, K+1):
    ans = ans * (N-i+1)/i
print(int(ans))