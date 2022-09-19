T = int(input())
for tc in range(1, T+1):
    a = input()
    arr = []
    anslst = []
    for i in range(len(a)//7):
        arr.append(a[7*i:7*i+8])
    for i in arr:
        ans = 0
        for j in range(7):
            if i[j] == '1':
                ans += 2 ** (6-j)
        anslst.append(ans)
    print(f'#{tc}', end=' ')
    print(*anslst)