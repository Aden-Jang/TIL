A, B, C = map(int,input().split())
a = A + B
ans = 1
if B >= C:
    ans = -1
    print(ans)
else:
    ans += A // (C - B)
    print(ans)