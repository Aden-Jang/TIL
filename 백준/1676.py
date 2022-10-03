N = int(input())
a = 1
while N:
    a *= N
    N -= 1
ans = 0
while True:
    if a % 10 == 0:
        a //= 10
        ans += 1
    else:
        break
print(ans)