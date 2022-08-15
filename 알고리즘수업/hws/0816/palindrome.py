T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = [list(str(input())) for _ in range(N)] # 문자열을 리스트로 받아옴
    ans = 0
    for i in range(N): # 행에서 회문 찾기
        for j in range(N-M+1): # 인덱스 0 ~ N-M까지
            if j == 0: # j-1이 -1이 되어 맨 마지막 값으로 나오기 때문에 맨 처음 값까지 보기 위함
                if a[i][j:j+M] == a[i][j+M-1::-1]:
                    ans = a[i][j:j+M]
            else:
                if a[i][j:j+M] == a[i][j+M-1:j-1:-1]:
                    ans = a[i][j:j+M]

    for i in range(N): # 전치시킴
        for j in range(N):
            if i < j:
                a[i][j], a[j][i] = a[j][i], a[i][j]

    for i in range(N): # 열에서 회문찾기
        for j in range(N-M+1):
            if j == 0:
                if a[i][j:j+M] == a[i][j+M-1::-1]:
                    ans = a[i][j:j+M]
            else:
                if a[i][j:j+M] == a[i][j+M-1:j-1:-1]:
                    ans = a[i][j:j+M]
    ans = ''.join(ans)
    print(f'#{tc} {ans}')