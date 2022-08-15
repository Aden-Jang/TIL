for tc in range(1, 11):
    N = int(input())
    a = [list(str(input())) for _ in range(8)] # 문자열을 리스트로 받아옴
    ans = 0
    for i in range(8): # 행에서 회문 찾기
        for j in range(8-N+1): # 인덱스 0 ~ 8-N까지
            if j == 0: # j-1이 -1이 되어 맨 마지막 값으로 나오기 때문에 맨 처음 값까지 보기 위함
                if a[i][j:j+N] == a[i][j+N-1::-1]:
                    ans += 1
            else:
                if a[i][j:j+N] == a[i][j+N-1:j-1:-1]:
                    ans += 1

    for i in range(8): # 전치시킴
        for j in range(8):
            if i < j:
                a[i][j], a[j][i] = a[j][i], a[i][j]

    for i in range(8): # 열에서 회문찾기
        for j in range(8-N+1):
            if j == 0:
                if a[i][j:j+N] == a[i][j+N-1::-1]:
                    ans += 1
            else:
                if a[i][j:j+N] == a[i][j+N-1:j-1:-1]:
                    ans += 1    
    print(f'#{tc} {ans}')