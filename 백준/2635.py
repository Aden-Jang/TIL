N = int(input())
ans = 0
if N == 0:
    print(0)
else:
    for i in range(0, N + 1):
        num = 2
        a = [N, N - i]
        while a[-2] - a[-1] >= 0:
            a.append(a[-2] - a[-1])
            num += 1

        if ans < num:
            ans = num
            anslst = a

    print(ans)
    print(*anslst)
