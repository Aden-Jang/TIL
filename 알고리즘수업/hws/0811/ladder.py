for _ in range(10):
    tc = int(input())
    a = [list(map(int,input().split())) for _ in range(100)]
    j = a[99].index(2)
    i = 99
    while i > 0: # i가 1일때 까지 반복(마지막에 위로 한칸은 무조건 가기 때문)
        if j == 99: # 오른쪽 끝에 있을 때
            if a[i][j-1] == 1: # 왼쪽이 1이면
                while a[i][j] == 1: # 0이 나올때 까지 계속 왼쪽으로 이동
                    j -= 1
                j += 1 # 0일 때 다시 1자리로 이동후 위로 한칸
                i -= 1
            else: # 위로한칸
                i -= 1
        elif j == 0: # 왼쪽 끝에 있을 때
            if a[i][j+1] == 1: # 오른쪽이 1이면
                while a[i][j] == 1: # 0이 나올때 까지 계속 오른쪽으로 이동
                    j += 1
                j -= 1  # 0일 때 다시 1자리로 이동후 위로 한칸
                i -= 1
            else:
                i -= 1
        else:
            if a[i][j-1] == a[i][j+1] == 0: # 양옆이 0이면 위로 한칸
                i -= 1
            elif a[i][j-1] == 1: # 왼쪽이 1이면 왼쪽 끝으로 이동후 위로한칸
                while a[i][j] == 1:
                    j -= 1
                    if j == -1:
                        break
                j += 1
                i -= 1
            elif a[i][j+1] == 1: # 오른쪽이 1이면 오른쪽 끝으로 이동후 위로한칸
                while a[i][j] == 1:
                    j += 1
                    if j == 100:
                        break
                j -= 1
                i -= 1
    print(f'#{tc} {j}')


T = 10
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int,input().split())) for _ in range(100)]
    for i in range(99): # 마지막이 2인 인덱스 추출, j에 대입
        if a[99][i] == 2:
            j = i
            break
    i = 99
    while i > 0:
        a[i][j] = 0 # 지나온 길은 0으로 바꿈
        if j > 0 and a[i][j-1] == 1: # 왼쪽이 끝이 아니고 1이면 왼쪽으로 한칸 이동
            j -= 1
        elif j < 99 and a[i][j+1] == 1: # 오른쪽이 끝이 아니고 1이면 오른쪽으로 한칸 이동
            j += 1
        else: # 양쪽다 1아니면 위로 한칸 이동
            i -= 1
    print(f'#{tc} {j}')
