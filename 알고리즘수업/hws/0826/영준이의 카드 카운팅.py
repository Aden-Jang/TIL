T = int(input())
for tc in range(1, T + 1):
    a = list(input())
    lst = []
    aaa = ''
    for i in range(len(a)):
        if i % 3 == 2:
            aaa = aaa + a[i]
            lst.append(aaa)
            aaa = ''
        else:
            aaa = aaa + a[i]
    lst.sort()

    s = d = h = c = 13
    for i in range(len(lst)):
        if i != len(lst) and lst[i] in lst[i+1:]:
            ans = 'ERROR'
            break
        else:
            if lst[i][0] == 'S':
                s -= 1
            elif lst[i][0] == 'D':
                d -= 1
            elif lst[i][0] == 'H':
                h -= 1
            elif lst[i][0] == 'C':
                c -= 1
        ans = str(s) + ' ' + str(d) + ' ' + str(h) + ' ' + str(c)
    print(f'#{tc} {ans}')
