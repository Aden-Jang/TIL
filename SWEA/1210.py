for _ in range(10):
    tc = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]
    j = a[99].index(2) # 마지막이 2인 값의 인덱스를 저장, 거기서부터 시작
    i = 99
    while i > 0: # 맨위에 도달할 때 까지
        a[i][j] = 0 # 지나온 자리는 0으로 표시해 되돌아 갈 수 없게 만듦
        if j == 99: # 오른쪽 끝에 있을 때는 왼쪽만 확인
            if a[i][j-1] == 1: # 왼쪽이 1이면 꺾음
                j -= 1
            else:
                i -=1
        elif j == 0: # 왼쪽 끝에 있을 때는 오른쪽만 확인
            if a[i][j+1] == 1: # 오른쪽이 1이면 꺾음
                j += 1
            else:
                i -=1
        else: # 양쪽 다 확인 한쪽이 1이면 꺾음
            if a[i][j+1] == 1:
                j += 1
            elif a[i][j-1] == 1:
                j -= 1
            else:
                i -=1
    print(f'#{tc} {j}')