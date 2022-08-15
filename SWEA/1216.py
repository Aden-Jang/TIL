for tc in range(1, 11):
    N = int(input())
    a = [list(str(input())) for _ in range(100)] # 문자열을 리스트로 받아옴
    ans = 0


    for i in range(100): # 전치시킴
        for j in range(100):
            if i < j:
                a[i][j], a[j][i] = a[j][i], a[i][j]


    print(f'#{tc} {ans}')
