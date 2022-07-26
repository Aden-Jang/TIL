T = int(input())
for i in range(T):
    a, b = input().split()
    a = list(map(int, a))
    b = int(b)
    for j in range(b):
        if max(a) 