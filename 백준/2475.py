a = list(map(int, input().split()))
ans = sum([n**2 for n in a]) % 10
print(ans)