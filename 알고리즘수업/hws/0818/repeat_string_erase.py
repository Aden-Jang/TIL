T = int(input())
for tc in range(1, T+1):
    a = list(input())
    i = 0
    while i != len(a) - 1:
        if a[i] == a[i+1]:
            a.pop(i+1)
            a.pop(i)
            if i == 0:
                pass
            else:
                i -= 1
        else:
            i += 1
    print(f'#{tc} {len(a)}')