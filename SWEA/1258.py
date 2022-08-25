T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    ijlst = []
    ansn = 0
    ans = []
    for i in range(N):
        for j in range(N):
            if (i, j) in ijlst:
                continue
            x = y = 0
            if a[i][j] != 0:
                o, p = i, j
                ijlst.append((i, j))
                while a[o][p] != 0:
                    x += 1
                    p += 1
                    if p == N:
                        break
                p -= 1
                while a[o][p] != 0:
                    y += 1
                    o += 1
                    if o == N:
                        break
                o -= 1
                ansn += 1
                ans.append((y,x))
                for k in range(i, i+y):
                    for l in range(j ,j+x):
                        ijlst.append((k, l))
    dic = {}
    for i in range(len(ans)):
        dic[ans[i]] = ans[i][0] * ans[i][1]
    aaa = sorted(dic.items(), key=lambda item: (item[1], item[0]))
    print(f'#{tc} {ansn}',end=' ')
    for i in range(len(aaa)):
        print(*aaa[i][0], end = ' ')
    print()