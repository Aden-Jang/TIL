for tc in range(1, 11):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for j in range(N):
        for i in range(N):
            if i != 99:
                if a[i][j] == 1: # i가 맨 아래가 아니고, N극일때
                    if a[i+1][j] != 2: # 바로 밑이 S극이 아니면 아래로 한칸 이동
                        a[i][j] = 0
                        a[i+1][j] = 1
                    else: # 바로 밑이 S극이면 이동을 멈추고 교착상태에 +1
                        ans += 1
            elif i != 0:
                if a[i][j] == 2: # i가 맨 위가 아니고 S극일때
                    if a[i - 1][j] != 1: # 바로 위가 N극이 아니면 위로 한칸 이동
                        a[i][j] = 0
                        a[i - 1][j] = 2
            if (i == 99 and a[i][j] == 1) or (i == 0 and a[i][j] == 2):
				# 맨 아래가 N극이거나 맨 위가 S극이면 아래로 떨어뜨림
                a[i][j] = 0
    print(f'#{tc} {ans}')