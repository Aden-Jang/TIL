A, B, C = map(int,input().split)
a = A + B
ans = 0
while a >= 0:
    ans += 1
    a = a + B - C
print(ans)