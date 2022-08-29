T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    stop = [0] * 1001
    for _ in range(N):
        bus, A, B = map(int, input().split())
        stop[A] += 1        # A, B에는 항상 정차
        stop[B] += 1
        if bus == 1:        # 일반
            for i in range(A + 1, B):
                stop[i] += 1
        elif bus == 2:      # 급행, A가 짝수 모든 짝수정류장
            # if A % 2 == 0:
            #     for i in range(A + 1, B):
            #         if i % 2 == 0:
            #             stop[i] += 1
            # else:
            #     for i in range(A + 1, B):
            #         if i % 2 == 1:
            #             stop[i] += 1

            for i in range(A + 2, B, 2):
                stop[i] += 1
        else:               # 광역
            if A % 2 == 0:
                for i in range(A + 1, B):
                    if i % 4 == 0:
                        stop[i] += 1
            else:
                for i in range(A + 1, B):
                    if i % 3 == 0 and i % 10 != 0:   # 3의 배수이면서 10의 배수가 아닌
                        stop[i] += 1
    print(f'#{tc} {max(stop)}')