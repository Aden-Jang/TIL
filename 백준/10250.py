T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    y = N % H
    if y == 0:
        y = str(H)
    x = N // H + 1
    if y == str(H):
        x -= 1
    x = str(x)
    if len(x) == 1:
        x = '0' + x
    print(str(y)+str(x))