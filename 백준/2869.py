A, B, V = map(int, input().split())
V -= A
ans = 1
if V % (A - B) == 0:
    ans += V // (A - B)
else:
    ans += V // (A - B) + 1
print(ans)