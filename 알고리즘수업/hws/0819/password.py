for tc in range(1, 11):
    N, a = input().split()
    ans = []
    for i in range(int(N)):
        if ans == []:
            ans.append(a[i])
        elif ans[-1] == a[i]:
            ans.pop()
        else:
            ans.append(a[i])
    ans = ''.join(ans)
    print(f'#{tc} {ans}')