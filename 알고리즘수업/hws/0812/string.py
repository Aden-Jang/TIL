for tc in range(1, 11):
    _ = int(input())
    ft = input()
    st = input()
    ans = 0
    i = 0
    for i in range(len(st)-len(ft)+1):
        if st[i:i+len(ft)] == ft:
            ans += 1
    print(f'#{tc} {ans}')