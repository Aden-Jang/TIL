for _ in range(10):
    tc = int(input())
    a = [list(map(int, input().split())) for _ in range(100)]
    for j in range(100):
        if a[0][j] == 1: # 시작이 1인 곳만 찾음
            i = 0 # 맨위로 이동(i값 초기화)
            n = j # 시작 j위치를 n에 저장
            d = 0 # 이동거리 초기화
            while i < 99:
                if j == 0: # 왼쪽 끝에 있으면
                    if a[i][j+1] == 1: # 오른쪽이 1이면
                        while a[i][j] == 1: # 오른쪽 끝이 0이 될때 까지 이동, 이동거리 추가
                            j += 1
                            d += 1
                        j -= 1
                        d -= 1
                        i += 1
                    else: # 아니면 밑으로 한칸 이동
                        i += 1
                elif j == 99: # 오른쪽 끝에 있으면
                    if a[i][j-1] == 1: # 왼쪽이 1이면
                        while a[i][j] == 1: # 왼쪽 끝이 0이 될때 까지 이동, 이동거리 추가
                            j -= 1
                            d += 1
                        j += 1
                        d -= 1
                        i += 1
                    else: # 아니면 밑으로 한칸 이동
                        i += 1
                else:
                    if a[i][j-1] == a[i][j+1] == 0: # 양쪽이 0이면 밑으로 한칸 이동
                        i += 1
                    elif a[i][j+1] == 1: # 오른쪽이 1이면
                        while a[i][j] == 1: # 끝이 0이 될때까지 이동, 이동거리 추가
                            j += 1
                            d += 1
                            if j == 100: # 오른쪽 끝까지 갔을 경우 빠져나옴
                                break
                        j -= 1
                        d -= 1
                        i += 1
                    elif a[i][j-1] == 1: # 왼쪽이 1이면
                        while a[i][j] == 1: # 끝이 0이 될때까지 이동, 이동거리 추가
                            j -= 1
                            d += 1
                            if j == -1: # 왼쪽 끝까지 갔을 경우 빠져나옴
                                break
                        j += 1
                        d -= 1
                        i +=1
            if n == 0: # mind와 ans를 맨 처음 값으로 넣어줌
                mind = d 
                ans = n
            else:
                if d < mind: # 이동거리가 그전까지의 가장 작은 이동거리보다 작으면 
                    mind = d # mind, ans 갱신
                    ans = n
    print(f'#{tc} {ans}')