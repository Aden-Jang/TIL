N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
d = len(A)
for i in A:
    i -= B
    if i <= 0 :
        continue
    else:
        if i % C:
            d += i // C + 1
        else:
            d += i // C
print(d)