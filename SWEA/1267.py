for tc in range(1, 11):
    V, E = map(int, input().split())
    a = list(map(int, input().split()))
    dic = {}
    lst = [[0] for _ in range(V+1)]
    for i in range(V+1):
        dic[i] = [0]
    for i in range(len(a)):
        if i % 2 == 1:
            dic[a[i]].append(a[i-1])
    ans = [0]
    i = 1
    while len(ans) <= V:
        if i in ans:
            i += 1
            continue
        for j in range(len(dic[i])):
            if dic[i][j] in ans:
                if j == len(dic[i])-1:
                    ans.append(i)
                    i = 1
            else:
                i = dic[i][j]
                break
    ans.pop(0)
    print(f'#{tc}', end = ' ')
    print(*ans)