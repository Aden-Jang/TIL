T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    maxn = 0
    for i in str1:
        inum = 0
        for j in str2:
            if i == j:
                inum += 1
        if inum > maxn:
            maxn = inum
    print(f'#{tc} {maxn}')